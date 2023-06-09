from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    DonateToProject,
    DonationListSerializer,
    TransactionListSerializer,
)
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from projects.models import Project
from rest_framework import generics, status, exceptions, serializers
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.db import transaction
from django.shortcuts import get_object_or_404
from .models import Payment
from rest_framework.authtoken.models import Token
from users.models import CustomUser

class DonateProjectView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = DonateToProject
    permission_classes = [AllowAny]
 
    def perform_create(self, serializer):
        try:
            authorization_header = self.request.headers.get("Authorization")
            if authorization_header is None:
                raise exceptions.NotAuthenticated(detail="Invalid Token.")
            token = authorization_header.split(" ")[1]
            user_id = Token.objects.get(key=token).user_id
        except Token.DoesNotExist:
            raise exceptions.NotAuthenticated(detail="Invalid token.")
        user = get_object_or_404(CustomUser, pk=user_id)
        serializer.save(user=user)
 
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            input_amount = serializer.validated_data.get("input_amount")
            project_id = serializer.validated_data.get("project").id
            if input_amount == 0 or input_amount is None:
                response_data = {
                    "status": 0,
                    "message": "You must enter a donation amount.",
                }
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
            else:
                try:
                    query = Project.objects.get(id=project_id)
                    if input_amount + query.current_amount > query.target_amount:
                        response_data = {
                            "status": 0,
                            "message": f"You cannot donate more than {query.target_amount - query.current_amount} to this project.",
                        }
                        return Response(
                            response_data, status=status.HTTP_400_BAD_REQUEST
                        )
 
                    query.current_amount += input_amount
                    query.save()
 
                    serializer.save()
                    response_data = {
                        "status": 1,
                        "message": "Donation successful.",
                        "data": serializer.data,
                    }
                    return Response(response_data, status=status.HTTP_201_CREATED)
                except serializers.ValidationError as e:
                    response_data = {"status": 0, "message": str(e)}
                    return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        else:
            response_data = {"status": 0, "errors": serializer.errors}
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        
class ProjectDonationAPI(generics.ListAPIView):
    serializer_class = DonationListSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["project_id"] = self.kwargs.get("project_id")
        return context

    def get_queryset(self):
        project_id = self.kwargs.get("project_id")
        project = get_object_or_404(Project, pk=project_id)
        try:
            donations = Payment.objects.filter(project=project).all()
            return [donations]
        except Payment.DoesNotExist:
            raise exceptions.NotFound(detail="No Donations in this project")


class UserTransactionAPI(generics.ListAPIView):
    serializer_class = TransactionListSerializer

    def get_queryset(self):
        try:
            authorization_header = self.request.headers.get("Authorization")
            if authorization_header is None:
                raise exceptions.NotAuthenticated(detail="Invalid Token.")
            token = authorization_header.split(" ")[1]
            user_id = Token.objects.get(key=token).user_id
            user = get_object_or_404(CustomUser, pk=user_id)
            try:
                donations = Payment.objects.filter(user=user).all()
                return [donations]
            except Payment.DoesNotExist:
                raise exceptions.NotFound(detail="No Donations Found.")
        except Token.DoesNotExist:
            raise exceptions.NotAuthenticated(detail="Invalid Token.")

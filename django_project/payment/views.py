from .models import Payment
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from users.models import CustomUser
from .serializers import DonateToProject, UpdateDonateProject
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from projects.models import Project
from rest_framework import serializers
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class DonateProjectView(generics.CreateAPIView):
    serializer_class = DonateToProject
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            input_amount = serializer.validated_data.get('input_amount')
            project_id = serializer.validated_data.get('project').id
            if input_amount == 0 or input_amount is None:
                response_data = {
                    "status": 0,
                    "message": "You must enter a donation amount."
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
                        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

                    query.current_amount += input_amount
                    query.save()

                    serializer.save()
                    response_data = {
                        "status": 1,
                        "message": "Donation successful.",
                        "data": serializer.data
                    }
                    return Response(response_data, status=status.HTTP_201_CREATED)
                except serializers.ValidationError as e:
                    response_data = {
                        "status": 0,
                        "message": str(e)
                    }
                    return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        else:
            response_data = {
                "status": 0,
                "errors": serializer.errors
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

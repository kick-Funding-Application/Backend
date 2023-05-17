from rest_framework import viewsets, generics
from .serializers import ProjectSerializer
from projects.models import Project
from rest_framework import filters, status, exceptions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from users.models import CustomUser
from django.shortcuts import get_object_or_404
from django.db.models import Q


# Create your views here.
class ProjectViewSets(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    search_fields = ["title", "details", "tags"]
    filter_backends = (filters.SearchFilter,)

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
        serializer.save(created_by=user, user_image=user.user_image)


class ProjectByCategoryAPI(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        try:
            category = self.kwargs.get("category")
            project = Project.objects.filter(category=category)
            return project
        except Project.DoesNotExist:
            return Project.objects.none()


class UserProjetAPI(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        try:
            authorization_header = self.request.headers.get("Authorization")
            if authorization_header is None:
                raise exceptions.NotAuthenticated(detail="Invalid Token.")
            token = authorization_header.split(" ")[1]
            user_id = Token.objects.get(key=token).user_id
            user = get_object_or_404(CustomUser, pk=user_id)
            project = Project.objects.filter(created_by=user)
            return project
        except Token.DoesNotExist:
            return exceptions.NotAuthenticated(detail="Invalid Token.")

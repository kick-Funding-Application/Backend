from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProjectSerializer, ThumbnailSerializer
from projects.models import Project


# Create your views here.
class ProjectViewSets(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

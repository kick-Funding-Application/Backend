from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import ProjectSerializer, ThumbnailSerializer
from projects.models import Project, Thumbnail


# Create your views here.
class ProjectViewSets(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ThumbnailViewSets(viewsets.ModelViewSet):
    queryset = Thumbnail.objects.all()
    serializer_class = ThumbnailSerializer

from rest_framework import viewsets, generics
from .serializers import ProjectSerializer, ThumbnailSerializer
from projects.models import Project, Thumbnail
from rest_framework import filters, status, exceptions
from common.serializers import RateSerializer, CommentSerializer
from common.models import Rate, Comment
from rest_framework.response import Response


# Create your views here.
class ProjectViewSets(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    search_fields = ["title", "details"]
    filter_backends = (filters.SearchFilter,)


class ThumbnailViewSets(viewsets.ModelViewSet):
    queryset = Thumbnail.objects.all()
    serializer_class = ThumbnailSerializer


class ProjectByCategoryAPI(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        try:
            category = self.kwargs.get("category")
            project = Project.objects.filter(category=category)
            return project
        except Project.DoesNotExist:
            return Project.objects.none()


class RateViewSets(viewsets.ModelViewSet):
    serializer_class = RateSerializer

    def get_queryset(self):
        try:
            project_id = int(self.kwargs.get("project_id"))
            project = Project.objects.get(pk=project_id)
            rate = Rate.objects.filter(project=project).all()
            if len(rate) == 0:
                raise exceptions.NotFound(detail="No rate for the current project.")
            return rate
        except Project.DoesNotExist:
            raise exceptions.NotFound(detail="Project Not found.")

    def perform_create(self, serializer):
        try:
            project_id = int(self.kwargs.get("project_id"))
            project = Project.objects.get(pk=project_id)
            serializer.save(project=project)
        except Project.DoesNotExist:
            raise exceptions.NotFound(detail="Project Not Found.")


class CommentViewSets(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        try:
            project_id = int(self.kwargs.get("project_id"))
            project = Project.objects.get(pk=project_id)
            comment = Comment.objects.filter(project=project).all()
            if len(comment) == 0:
                raise exceptions.NotFound(detail="No comment for the current project.")
            return comment
        except Project.DoesNotExist:
            raise exceptions.NotFound(detail="Project Not found.")

from rest_framework import viewsets, generics
from .serializers import ProjectSerializer, ThumbnailSerializer
from projects.models import Project, Thumbnail
from rest_framework import filters, status, exceptions
from common.serializers import RateSerializer, CommentSerializer
from common.models import Rate, Comment
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from users.models import CustomUser
from django.shortcuts import get_object_or_404
from django.db.models import Q


# Create your views here.
class ProjectViewSets(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    search_fields = ["title", "details"]
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
        serializer.save(created_by=user)


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
            project = get_object_or_404(Project, pk=project_id)

            authorization_header = self.request.headers.get("Authorization")
            if authorization_header is None:
                raise exceptions.NotAuthenticated(detail="Invalid Token.")
            token = authorization_header.split(" ")[1]
            user_id = Token.objects.get(key=token).user_id
            user = get_object_or_404(CustomUser, pk=user_id)

            rate = Rate.objects.filter(Q(project=project) & Q(user=user)).first()
            if rate is not None and rate.user == user:
                raise exceptions.PermissionDenied(detail="Not allowed to rate twice.")

        except Token.DoesNotExist:
            raise exceptions.NotAuthenticated(detail="Invalid Token.")
        serializer.save(project=project, user=user)

        return Response({"detail": "Thank You for rating :)"}, status=201)


class CommentViewSets(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        try:
            project_id = int(self.kwargs.get("project_id"))
            project = Project.objects.get(pk=project_id)
            comment = Comment.objects.filter(project=project).all()
            if len(comment) == 0.0:
                raise exceptions.NotFound(detail="No comment for the current project.")
            return comment
        except Project.DoesNotExist:
            raise exceptions.NotFound(detail="Project Not found.")

    def perform_create(self, serializer):
        try:
            project_id = int(self.kwargs.get("project_id"))
            project = get_object_or_404(Project, pk=project_id)

            authorization_header = self.request.headers.get("Authorization")
            if authorization_header is None:
                raise exceptions.NotAuthenticated(detail="Invalid Token.")
            token = authorization_header.split(" ")[1]
            user_id = Token.objects.get(key=token).user_id
            user = get_object_or_404(CustomUser, pk=user_id)

            comment = Comment.objects.filter(Q(project=project) & Q(user=user)).first()
            if comment is not None and comment.user == user:
                raise exceptions.PermissionDenied(detail="Not allowed to rate twice.")
        except Project.DoesNotExist:
            raise exceptions.NotAuthenticated(detail="Invalid Token.")

        serializer.save(project=project, user=user)

        return Response({"detail": "Thank You for Commenting :)"}, status=201)

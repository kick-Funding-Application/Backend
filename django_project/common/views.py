from django.shortcuts import render
from .models import Feedback
from .serializers import FeedbackSerializer
from rest_framework import viewsets, exceptions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.db.models import Q
from projects.models import Project
from users.models import CustomUser


# Create your views here.
class FeedbackViewSets(viewsets.ModelViewSet):
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        try:
            project_id = int(self.kwargs.get("project_id"))
            project = Project.objects.get(pk=project_id)
            feedback = Feedback.objects.filter(project=project).all()
            if len(feedback) == 0:
                raise exceptions.NotFound(detail="No feedback for the current project.")
            return feedback
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

            feedback = Feedback.objects.filter(
                Q(project=project) & Q(user=user)
            ).first()
            if feedback is not None and feedback.user == user:
                raise exceptions.PermissionDenied(
                    detail="Not allowed to feedback twice."
                )

        except Token.DoesNotExist:
            raise exceptions.NotAuthenticated(detail="Invalid Token.")
        serializer.save(project=project, user=user)

        return Response({"detail": "Thank You for rating :)"}, status=201)

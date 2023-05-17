from rest_framework import serializers, exceptions
from .models import Feedback
from rest_framework.response import Response


# class RateSerializer(serializers.ModelSerializer):
#     user = serializers.CharField(required=False)
#     project = serializers.CharField(required=False)

#     class Meta:
#         model = Rate
#         fields = ("value", "user", "project")


# class CommentSerializer(serializers.ModelSerializer):
#     created_dt = serializers.DateTimeField(format="%B %d, %Y %I:%M %p", read_only=True)
#     user = serializers.CharField(required=False)
#     project = serializers.CharField(required=False)

#     class Meta:
#         model = Comment
#         fields = ("content", "created_dt", "user", "project")


class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.CharField(required=False)
    project = serializers.CharField(required=False)
    created_dt = serializers.DateField(read_only=True)

    class Meta:
        model = Feedback
        fields = "__all__"

from rest_framework import serializers
from .models import Rate, Comment


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ("value", "user", "project")


class CommentSerializer(serializers.ModelSerializer):
    created_dt = serializers.DateTimeField(format="%B %d, %Y %I:%M %p", read_only=True)

    class Meta:
        model = Comment
        fields = ("content", "created_dt", "user")

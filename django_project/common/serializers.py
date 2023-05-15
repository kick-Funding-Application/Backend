from rest_framework import serializers, exceptions
from .models import Rate, Comment
from rest_framework.response import Response


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ("value", "user", "project")

    def create(self, validated_data):
        user_id = validated_data["user"]
        project_id = validated_data["project"]
        rate = Rate.objects.filter(project=project_id).first()
        if rate is not None and rate.user == user_id:
            raise exceptions.PermissionDenied(detail="Not allowed to rate twice.")
        Rate.objects.create(**validated_data)
        return Response({"detail": "Thank You for rating :)"}, status=201)


class CommentSerializer(serializers.ModelSerializer):
    created_dt = serializers.DateTimeField(format="%B %d, %Y %I:%M %p", read_only=True)

    class Meta:
        model = Comment
        fields = ("content", "created_dt", "user", "project")

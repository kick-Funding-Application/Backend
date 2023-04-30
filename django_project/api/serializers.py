from rest_framework import serializers
from ..projects.models import Project, Thumbnail


class ThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnail
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()
    end_date = serializers.DateTimeField(format="%B %d, %Y %I:%M %p", required=False)

    class Meta:
        model = Project
        fields = ("title", "details", "end_date", "category", "tags")

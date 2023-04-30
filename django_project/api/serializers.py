from rest_framework import serializers
from projects.models import Thumbnail, Project


class ThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnail
        fields = ("image_url",)


class ProjectSerializer(serializers.ModelSerializer):
    end_date = serializers.DateTimeField(format="%B %d, %Y %I:%M %p", required=False)
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "details",
            "end_date",
            "category",
            "tags",
            "img_url",
        )

    def get_img_url(self, obj):
        image_url = obj.get_img_url()
        if image_url:
            serializer = ThumbnailSerializer(image_url, many=True)
            return serializer.data
        return None

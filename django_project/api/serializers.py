from rest_framework import serializers
from projects.models import Thumbnail, Project


class ThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnail
        fields = ("image_url",)


# class ProjectInputSerializer(serializers.ModelSerializer):
#     thumbnails = ThumbnailSerializer(many=True)
#
#     class Meta:
#         model = Project
#         fields = (
#             "title",
#             "details",
#             "target_amount",
#             "end_date",
#             "category",
#             "tags",
#             "thumbnails",
#         )


class ProjectSerializer(serializers.ModelSerializer):
    end_date = serializers.DateTimeField(format="%B %d, %Y %I:%M %p", required=False)
    img_url = serializers.SerializerMethodField()
    thumbnails = ThumbnailSerializer(many=True, write_only=True)

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "details",
            "target_amount",
            "end_date",
            "category",
            "tags",
            "img_url",
            "thumbnails",
        )

    def get_img_url(self, obj):
        image_url = obj.get_img_url()
        if image_url:
            serializer = ThumbnailSerializer(image_url, many=True)
            return serializer.data
        return None

    def create(self, validated_data):
        thumbnail_data = validated_data.pop("thumbnails")
        project = Project.objects.create(**validated_data)
        for data in thumbnail_data:
            Thumbnail.objects.create(project=project, **data)
        return project
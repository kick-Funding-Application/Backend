from rest_framework import serializers, status, exceptions
from projects.models import Thumbnail, Project
from users.models import CustomUser
from common.models import Rate, Comment
from common.serializers import CommentSerializer


class ThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnail
        fields = ("image",)


class ProjectSerializer(serializers.ModelSerializer):
    end_date = serializers.DateTimeField(format="%B %d, %Y %I:%M %p", required=False)
    thumbnails = ThumbnailSerializer(write_only=True)
    img_url = serializers.SerializerMethodField()
    rate = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "details",
            "created_by",
            "target_amount",
            "current_amount",
            "end_date",
            "category",
            "tags",
            "comments",
            "rate",
            "img_url",
            "thumbnails",
        )

    def get_img_url(self, obj):
        image_url = obj.get_img_url()
        if image_url:
            serializer = ThumbnailSerializer(image_url)
            return serializer.data
        return "No image found."

    def get_rate(self, obj):
        counts = {}
        for i in range(1, 6):
            cnt = Rate.objects.filter(project=obj, value=i).count()
            counts[i] = cnt
        num_1 = counts.get(1, 0)
        num_2 = counts.get(2, 0)
        num_3 = counts.get(3, 0)
        num_4 = counts.get(4, 0)
        num_5 = counts.get(5, 0)
        try:
            avg_rate = (num_5 * 5 + num_4 * 4 + num_3 * 3 + num_2 * 2 + num_1 * 1) / (
                float(num_5 + num_4 + num_3 + num_2 + num_1)
            )
        except ZeroDivisionError:
            avg_rate = 0
        rate_data = {
            "num_1": num_1,
            "num_2": num_2,
            "num_3": num_3,
            "num_4": num_4,
            "num_5": num_5,
            "avg_rate": round(avg_rate, 2),
        }
        return rate_data

    def get_comments(self, obj):
        comments = Comment.objects.filter(project=obj.pk).all()
        if comments:
            serializer = CommentSerializer(comments, many=True)
            return serializer.data
        return "No comments yet."

    def create(self, validated_data):
        try:
            thumbnail_data = validated_data.pop("thumbnails")["image"]
            project = Project.objects.create(**validated_data)
            Thumbnail.objects.create(project=project, image=thumbnail_data)
            return project
        except Exception as e:
            raise exceptions.ParseError(detail=str(e))

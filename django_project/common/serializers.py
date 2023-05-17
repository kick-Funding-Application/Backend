from rest_framework import serializers, exceptions
from .models import Feedback
from rest_framework.response import Response


class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.CharField(required=False)
    user_image = serializers.SerializerMethodField("get_user_image")
    project = serializers.CharField(required=False)
    created_dt = serializers.DateField(read_only=True)

    class Meta:
        model = Feedback
        fields = (
            "id",
            "user",
            "user_image",
            "project",
            "created_dt",
            "rate",
            "content",
        )

    def get_user_image(self, obj):
        return obj.user_image

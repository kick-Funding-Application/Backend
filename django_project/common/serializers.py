from rest_framework import serializers
from .models import Rate, Comment


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    created_dt = serializers.DateTimeField(format="%B %d, %Y %I:%M %p", required=False)

    class Meta:
        model = Comment
        fields = "__all__"

from rest_framework import serializers, status, exceptions
from projects.models import Project
from users.models import CustomUser
from common.models import Feedback
from common.serializers import FeedbackSerializer


class ProjectSerializer(serializers.ModelSerializer):
    end_date = serializers.DateField(required=False)
    start_date = serializers.DateField(read_only=True, required=False)
    rate = serializers.SerializerMethodField()
    feedback = serializers.SerializerMethodField()
    created_by = serializers.CharField(required=False)

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "details",
            "created_by",
            "target_amount",
            "current_amount",
            "start_date",
            "end_date",
            "category",
            "tags",
            "image",
            "rate",
            "feedback",
        )

    def get_rate(self, obj):
        counts = {}
        for i in range(1, 6):
            cnt = Feedback.objects.filter(project=obj, rate=i).count()
            counts[i] = cnt
        rate_sum = 0
        total_sum = 0
        for i in range(1, 6):
            rate_sum += i * counts.get(i, 0)
            total_sum += counts.get(i, 0)
        # num_1 = counts.get(1, 0)
        # num_2 = counts.get(2, 0)
        # num_3 = counts.get(3, 0)
        # num_4 = counts.get(4, 0)
        # num_5 = counts.get(5, 0)
        try:
            avg_rate = rate_sum / float(total_sum)
        except ZeroDivisionError:
            avg_rate = 0
        rate_data = {
            # "num_1": num_1,
            # "num_2": num_2,
            # "num_3": num_3,
            # "num_4": num_4,
            # "num_5": num_5,
            "avg_rate": round(avg_rate, 2),
        }
        return rate_data

    def get_feedback(self, obj):
        feedback = Feedback.objects.filter(project=obj.pk).all()
        if feedback:
            serializer = FeedbackSerializer(feedback, many=True)
            return serializer.data
        return "No feedback yet."

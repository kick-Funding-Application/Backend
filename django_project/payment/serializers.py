from rest_framework import exceptions, serializers
from .models import Payment
from projects.models import Project
from django.shortcuts import get_object_or_404


class DonateToProject(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            "input_amount",
            "project",
            "user",
            "created_at",
            "target_amount",
            "current_amount",
        )


class UpdateDonateProject(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ("current_amount",)


class DonateInfoSerializer(serializers.ModelSerializer):
    value = serializers.FloatField(source="input_amount")
    user = serializers.StringRelatedField()

    class Meta:
        model = Payment
        fields = ("value", "user")


class DonateDateSerializer(serializers.ModelSerializer):
    date = serializers.DateField(source="created_at")
    info = DonateInfoSerializer(many=True)

    class Meta:
        model = Payment
        fields = ("date", "info")


class DonationListSerializer(serializers.Serializer):
    donation_list = DonateDateSerializer(many=True)

    def get_donation_list(self, obj):
        donations = obj

        result = {}
        for donation in donations:
            date = donation.created_at.strftime("%Y-%m-%d")
            info_serializer = DonateInfoSerializer(donation)
            info_data = info_serializer.data

            if date in result:
                result[date].append(info_data)
            else:
                result[date] = [info_data]

        return result

    def to_representation(self, instance):
        if len(self.get_donation_list(instance)) != 0:
            return {"donation_list": self.get_donation_list(instance)}
        else:
            raise exceptions.NotFound(detail="No Donations Found.")

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
        read_only_fields = ("user",)  # Exclude 'user' from being required

    def validate(self, attrs):
        attrs["user"] = self.context["request"].user  # Set the user from the request
        return attrs

class UpdateDonateProject(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ("current_amount",)


class DonateInfoSerializer(serializers.ModelSerializer):
    amount = serializers.FloatField(source="input_amount")
    user = serializers.StringRelatedField()
    phone_number = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = ("amount", "user", "phone_number")

    def get_phone_number(self, obj):
        return obj.user.phone_number


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


class UserTransactionInfoSerializer(serializers.ModelSerializer):
    amount = serializers.FloatField(source="input_amount")
    project = serializers.StringRelatedField()
    details = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = ("amount", "project", "details")

    def get_details(self, obj):
        return obj.project.details


class UserTransactionDateSerializer(serializers.ModelSerializer):
    date = serializers.DateField(source="created_at")
    info = UserTransactionInfoSerializer(many=True)

    class Meta:
        model = Payment
        fields = ("date", "info")


class TransactionListSerializer(serializers.Serializer):
    transaction_list = UserTransactionDateSerializer(many=True)

    def get_transaction_list(self, obj):
        transactions = obj
        response = {}
        for transaction in transactions:
            date = transaction.created_at.strftime("%Y-%m-%d")
            serializer = UserTransactionInfoSerializer(transaction)
            data = serializer.data

            if date in response:
                response[date].append(data)
            else:
                response[date] = [data]
        return response

    def to_representation(self, instance):
        if len(self.get_transaction_list(instance)) != 0:
            return {"transaction_list": self.get_transaction_list(instance)}
        else:
            raise exceptions.NotFound(detail="No Donations Found.")

from email.policy import default
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django_countries.serializer_fields import CountryField
from django.conf import settings
import datetime

User = settings.AUTH_USER_MODEL


class CustomRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(max_length=150)
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    phone_number = serializers.IntegerField()
    country = CountryField()
    user_image = serializers.CharField(required=False)
    birth_date = serializers.DateField()

    def custom_signup(self, request, user):
        user.username = self.validated_data["username"]
        user.first_name = self.validated_data["first_name"]
        user.last_name = self.validated_data["last_name"]
        user.phone_number = self.validated_data["phone_number"]
        user.country = self.validated_data.get("country")
        user.user_image = self.validated_data.get("user_image")
        user.birth_date = self.validated_data["birth_date"]

        user.save()

class CustomUserDetailsSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.CharField(max_length=150)
    first_name = serializers.CharField(max_length=20, required=False)
    last_name = serializers.CharField(max_length=20, required=False)
    phone_number = serializers.IntegerField(required=False)
    country = CountryField(required=False)
    user_image = serializers.CharField(required=False)
    birth_date = serializers.DateField(required=False)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.phone_number = validated_data.get("phone_number", instance.phone_number)
        instance.country = validated_data.get("country", instance.country)
        instance.user_image = validated_data.get("user_image", instance.user_image)
        instance.birth_date = validated_data.get("birth_date", instance.birth_date)
        instance.save()
        return instance


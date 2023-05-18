from django.contrib.auth import get_user_model
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import UserDetailsView
from users.serializers import CustomRegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC
from .serializers import CustomUserDetailsSerializer
from rest_framework import status
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.crypto import get_random_string


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response(
                {"detail": "You are already registered and logged in."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().post(request, *args, **kwargs)



class CustomUserDetailsView(UserDetailsView):
    serializer_class = CustomUserDetailsSerializer


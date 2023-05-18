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

    def perform_create(self, serializer):
        user = serializer.save(self.request)

        # Get the current site
        current_site = get_current_site(self.request)

        # Create the email confirmation instance
        email_address = user.emailaddress_set.get(email=user.email)
        email_confirmation = EmailConfirmation.create(email_address)
        email_confirmation.sent = timezone.now()
        email_confirmation.key = get_random_string(length=40)  # Generate a unique key
        email_confirmation.save()

        # Build the confirmation URL
        confirmation_url = reverse(
            'email-confirmation', kwargs={'key': email_confirmation.key})
        confirmation_url = f"http://127.0.0.1:8000{confirmation_url}"

        # Send the email
        send_mail(
            'Email Confirmation For Kick Funding App',
            f'Please confirm your email by clicking the following link: {confirmation_url}',
            'your-email@gmail.com',
            [user.email],
            fail_silently=False,
        )


class CustomUserDetailsView(UserDetailsView):
    serializer_class = CustomUserDetailsSerializer


class EmailConfirmationView(APIView):
    def get(self, request, key):
        try:
            email_confirmation = self.get_email_confirmation(key)
        except EmailConfirmation.DoesNotExist:
            return Response({'error': 'Invalid key'}, status=status.HTTP_400_BAD_REQUEST)

        if email_confirmation.email_address.verified:
            return Response({'message': 'Email already verified'}, status=status.HTTP_200_OK)

        email_confirmation.confirm()
        user = self.get_user(email_confirmation)

        # Perform additional actions if needed, such as updating user fields
        user.is_active = True
        user.save()

        return Response({'message': 'Email confirmed successfully'}, status=status.HTTP_200_OK)

    def get_email_confirmation(self, key):
        email_confirmation = EmailConfirmationHMAC.from_key(key)
        if not email_confirmation:
            raise EmailConfirmation.DoesNotExist
        return email_confirmation

    def get_user(self, email_confirmation):
        User = get_user_model()
        return User.objects.get(email=email_confirmation.email_address.email)

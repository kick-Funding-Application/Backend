from django.contrib.auth import get_user_model
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import UserDetailsView
from users.serializers import CustomRegisterSerializer
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC
from .serializers import CustomUserDetailsSerializer
from rest_framework import status


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

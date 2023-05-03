from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser  # from the current dir import it
from logging import PlaceHolder
from tkinter import Widget
from django import forms
from allauth.account.forms import SignupForm
from django_countries.fields import CountryField
from django.conf import settings

User = settings.AUTH_USER_MODEL


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(
        max_length=30, help_text='Enter Your Fisrt Name')
    last_name = forms.CharField(
        max_length=30, help_text='Enter Your Last Name')
    phone_number = forms.CharField(
        max_length=14, required=False, help_text='Optional')
    country = CountryField().formfield()
    user_image = forms.ImageField(required=False)
    birth_date = forms.DateTimeField()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        # this name from the customized models
        fields = UserCreationForm.Meta.fields + \
            ("first_name", "last_name", "phone_number")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

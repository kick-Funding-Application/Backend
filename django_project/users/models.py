from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.IntegerField(null=True, blank=True)
    country = CountryField(null=True, blank=True)
    user_image = models.CharField(max_length=500, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return super().__str__()

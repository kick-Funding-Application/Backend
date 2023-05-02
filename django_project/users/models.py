from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserCustom(AbstractUser):
    pass
# TODO
# AUTH_USER_MODEL =  "users.CustomUser"

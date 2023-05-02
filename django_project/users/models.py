from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    # Specify unique related_names for groups and user_permissions fields
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_users',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_users',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
        related_query_name='custom_user',
    )
    first_name = models.CharField(null=True, blank=True, max_length=100)
    last_name = models.CharField(null=True, blank=True, max_length=100)
    phone_number = models.PositiveIntegerField(null=True, blank=True)

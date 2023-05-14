from django.db import models
from projects.models import Project
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import Truncator
from django.conf import settings


# Create your models here.
class Rate(models.Model):
    value = models.IntegerField(
        default=0, validators=[MaxValueValidator(5), MinValueValidator(0)]
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return f"{self.user} rate {self.project.title} by {self.value}"


class Comment(models.Model):
    content = models.CharField(max_length=2500)
    created_dt = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return Truncator(self.content).chars(50)

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import Truncator
from django.conf import settings
from projects.models import Project


class Feedback(models.Model):
    rate = models.IntegerField(
        default=0, validators=[MaxValueValidator(5), MinValueValidator(0)]
    )
    content = models.CharField(max_length=2500, null=True, blank=True)
    created_dt = models.DateField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return f"{self.user} rate {self.project.title} by {self.rate}"

    @property
    def user_image(self):
        if self.user and hasattr(self.user, "user_image"):
            return self.user.user_image
        return None

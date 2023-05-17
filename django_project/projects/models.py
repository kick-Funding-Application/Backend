from django.db import models

from django.conf import settings


# Create your models here.
class Project(models.Model):
    CATEGORY_CHOICES = [
        ("Health", "Health"),
        ("Education", "Education"),
        ("Environment", "Environment"),
        ("Animals", "Animals"),
        ("Culture & Art", "Culture & Art"),
        ("Other", "Other"),
    ]

    title = models.CharField(max_length=150, unique=True)
    details = models.TextField()
    target_amount = models.PositiveIntegerField(default=0)
    current_amount = models.IntegerField(default=0)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    image = models.CharField(max_length=250, null=True, blank=True)
    created_dt = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )
    category = models.CharField(
        max_length=50, choices=CATEGORY_CHOICES, default="other"
    )
    tags = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title

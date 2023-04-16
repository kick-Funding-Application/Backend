from django.db import models


# Create your models here.
class Project(models.Model):
    CATEGORY_CHOICES = [
        ("health", "Health"),
        ("education", "Education"),
        ("environment", "Environment"),
        ("animal", "Animal"),
        ("culture & art", "Culture & Art"),
        ("other", "Other"),
    ]

    title = models.CharField(max_length=150, unique=True)
    details = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    created_dt = models.DateTimeField(auto_now_add=True)
    category = models.CharField(
        max_length=50, choices=CATEGORY_CHOICES, default="other"
    )
    tags = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title


class Thumbnail(models.Model):
    image_url = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.project.__str__()

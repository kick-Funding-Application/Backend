from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100, unique=True)
    details = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    created_dt = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title

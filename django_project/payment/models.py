from django.db import models
from users.models import CustomUser
from projects.models import Project


class Payment(models.Model):
    input_amount = models.FloatField(null=True)
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f"{self.user} Donate to {self.project}")

    @property
    def target_amount(self):
        return self.project.target_amount

    @property
    def current_amount(self):
        return self.project.current_amount

# class Donations(models.Model):
#     paid_up = models.IntegerField()
#     project = models.ForeignKey(Projects, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return (f"{self.user} Donate to {self.project}")

# class Projects(models.Model):
#     title = models.CharField(max_length=250, unique=True)
#     details = models.TextField()
#     rate = models.IntegerField()
#     total_target = models.IntegerField()
#     current_donation = models.IntegerField()
#     start_campaign = models.DateTimeField(default=timezone.now)
#     end_campaign = models.DateField()
#     created_at = models.DateTimeField(default=timezone.now)
#     selected_at_by_admin = models.DateTimeField(default=timezone.now)
#     category = models.ForeignKey(Categories, on_delete=models.CASCADE)
#     owner = models.ForeignKey(User,  on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title

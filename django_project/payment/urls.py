from django.urls import path
from .views import DonateProjectView, ProjectDonationAPI

urlpatterns = [
    path("donate/", DonateProjectView.as_view(), name="donate"),
    path(
        "donate/<int:project_id>/history/",
        ProjectDonationAPI.as_view(),
        name="donation_list",
    ),
]

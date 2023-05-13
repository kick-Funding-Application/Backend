from django.urls import path
from .views import DonateProjectView

urlpatterns = [
    path('donate/', DonateProjectView.as_view(), name='donate'),
]

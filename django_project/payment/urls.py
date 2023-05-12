from django.urls import path, include
from .views import DonateProjectView

urlpatterns = [
    path('donate/', DonateProjectView.as_view(), name='donate'),
]

from users.views import CustomUserDetailsView
from .views import (
    ProjectViewSets,
    ThumbnailViewSets,
    ProjectByCategoryAPI,
)
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from dj_rest_auth.registration.views import VerifyEmailView
from dj_rest_auth.views import (
    PasswordChangeView, PasswordResetView, PasswordResetConfirmView, LogoutView)
from users.views import (
    CustomRegisterView, CustomUserDetailsView, EmailConfirmationView)


router = DefaultRouter()
router.register("projects", ProjectViewSets, basename="project")
router.register("images", ThumbnailViewSets, basename="image")


urlpatterns = [
    path('dj-rest-auth/password/reset/', PasswordResetView.as_view(),
         name='rest_password_reset'),
    path('dj-rest-auth/password/reset/confirm/', PasswordResetConfirmView.as_view(),
         name='rest_password_reset_confirm'),
    path("", include(router.urls)),
    path(
        "projects/<str:category>/filter",
        ProjectByCategoryAPI.as_view(),
        name="project_list",
    ),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path('dj-rest-auth/registration/',
         CustomRegisterView.as_view(), name='rest_register'),
    path("api/dj-rest-auth/user/",
         CustomUserDetailsView().as_view(), name='user-details'),
    path('', include('django.contrib.auth.urls')),
]

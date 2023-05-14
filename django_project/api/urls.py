from users.views import CustomUserDetailsView
from .views import (
    ProjectViewSets,
    ThumbnailViewSets,
    ProjectByCategoryAPI,
    RateViewSets,
    CommentViewSets,
)
from dj_rest_auth.registration.views import VerifyEmailView
from rest_framework.routers import DefaultRouter
from django.urls import path, include, re_path
from dj_rest_auth.views import (
    PasswordChangeView,
    PasswordResetView,
    PasswordResetConfirmView,
)
from users.views import CustomRegisterView, CustomUserDetailsView, EmailConfirmationView


router = DefaultRouter()
router.register("projects", ProjectViewSets, basename="project")
router.register("images", ThumbnailViewSets, basename="image")
router.register("rate", RateViewSets, basename="rate")
router.register("comment", CommentViewSets, basename="comment")


urlpatterns = [
    path("password/reset/", PasswordResetView.as_view(), name="rest_password_reset"),
    path(
        "password/reset/confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path("", include(router.urls)),
    path(
        "projects/<str:category>/filter",
        ProjectByCategoryAPI.as_view(),
        name="project_list",
    ),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path(
        "dj-rest-auth/registration/", CustomRegisterView.as_view(), name="rest_register"
    ),
    re_path(
        "account-confirm-email/",
        VerifyEmailView.as_view(),
        name="account_email_verification_sent",
    ),
    re_path(
        "account-confirm-email/(?P<key>[-:\w]+)/$",
        VerifyEmailView.as_view(),
        name="account_confirm_email",
    ),
    path(
        "email-confirmation/<str:key>/",
        EmailConfirmationView.as_view(),
        name="email-confirmation",
    ),
    path("dj-rest-auth/user/", CustomUserDetailsView().as_view(), name="user-details"),
    path("", include("payment.urls")),
]

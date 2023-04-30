from .views import ProjectViewSets, ThumbnailViewSets
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()
router.register("projects", ProjectViewSets)
router.register("images", ThumbnailViewSets)

urlpatterns = [
    path("", include(router.urls)),
]

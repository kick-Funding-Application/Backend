from .views import ProjectViewSets, ThumbnailViewSets, ProjectByCategoryAPI
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()
router.register("projects", ProjectViewSets, basename="project")
router.register("images", ThumbnailViewSets, basename="image")


urlpatterns = [
    path("", include(router.urls)),
    path(
        "projects/<str:category>/filter",
        ProjectByCategoryAPI.as_view(),
        name="project_list",
    ),
]

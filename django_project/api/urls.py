from .views import ProjectViewSets, ThumbnailViewSets, ProjectByCatergoryAPI
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()
router.register("projects", ProjectViewSets, basename="projects")
router.register("images", ThumbnailViewSets, basename="images")


urlpatterns = [
    path("", include(router.urls)),
    path(
        "projects/<str:category>/list",
        ProjectByCatergoryAPI.as_view(),
        name="project_list",
    ),
]

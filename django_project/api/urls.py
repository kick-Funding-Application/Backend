from .views import ProjectViewSets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("projects", ProjectViewSets)

urlpatterns = router.urls

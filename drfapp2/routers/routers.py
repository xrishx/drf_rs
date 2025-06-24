from rest_framework.routers import DefaultRouter
from ..viewsets.drfapp2_viewsets import AuthorViewsets as drfapp2_viewsets

router = DefaultRouter()
router.register('drfapp2', drfapp2_viewsets, basename='drfapp2')

urlpatterns = router.urls
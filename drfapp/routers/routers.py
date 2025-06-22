from rest_framework.routers import DefaultRouter
from ..viewsets.drfapp_viewsets import bookViewsets as drfapp_viewsets

router = DefaultRouter()

router.register('drfapp', drfapp_viewsets, basename='drfapp')

urlpatterns = router.urls
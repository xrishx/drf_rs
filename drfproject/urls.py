"""
URL configuration for drfproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from drfapp.viewsets.drfapp_viewsets import bookViewsets 
import drfapp.viewsets.drfapp_viewsets
from drfapp2.viewsets.drfapp2_viewsets import AuthorViewsets
import drfapp.viewsets
# from drfapp.routers.routers import router as drfapp_router
# from drfapp2.routers.routers import router as drfapp2_router    

router = routers.DefaultRouter()

router.register('drfapp', bookViewsets, basename='drfapp')
router.register('drfapp2', AuthorViewsets, basename='drfapp2')

# Documentation for API using drf_yasg
schema_view = get_schema_view(
    openapi.Info(
        title="DRF Project API",
        default_version='v1',
        description="API documentation for the DRF project by Rishav Shrestha",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="rishavshrestha6679@gmail.com"),
        license=openapi.License(name="No License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    # API Authentication and Documentation
    # api/ go to the API documentation
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('api/', include(drfapp_router.urls)),
    # path('api/', include(drfapp2_router.urls)),
    # Swagger Documentation
    # just api go to the Swagger UI
    path('',schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('simple', drfapp.viewsets.drfapp_viewsets.simple_view),
]

# Need this to correctly view media files in development
if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
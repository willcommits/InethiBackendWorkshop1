from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NetworkDeviceViewSet, ServiceViewSet

router = DefaultRouter()
router.register(r'devices', NetworkDeviceViewSet)
router.register(r'services', ServiceViewSet)

urlpatterns = [ path('', include(router.urls)) ]

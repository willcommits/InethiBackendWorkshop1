from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NetworkDeviceViewSet, ServiceViewSet, AlertsViewSet

router = DefaultRouter()
router.register(r'devices', NetworkDeviceViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'alerts', AlertsViewSet)

urlpatterns = [ path('', include(router.urls)) ]

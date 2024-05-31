
from rest_framework.viewsets import ModelViewSet

from .models import NetworkDevice, Service, Alert
from .serializers import NetworkDeviceSerializer, ServiceSerializer, AlertSerializer


class NetworkDeviceViewSet(ModelViewSet):
    """View/Edit/Add/Delete NetworkDevice items."""

    queryset = NetworkDevice.objects.all()
    serializer_class = NetworkDeviceSerializer



class ServiceViewSet(ModelViewSet):
    """View/Edit/Add/Delete Service items."""

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class AlertsViewSet(ModelViewSet):
    """View/Edit/Add/Delete Alert items."""

    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

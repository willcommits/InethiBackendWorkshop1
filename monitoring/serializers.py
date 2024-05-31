from rest_framework.serializers import ModelSerializer

from .models import NetworkDevice, Service, Alert


class NetworkDeviceSerializer(ModelSerializer):
    """Serializes NetworkDevice objects from django model to JSON."""

    class Meta:
        """NetworkDeviceSerializer metadata."""
        model = NetworkDevice
        fields = "__all__"


class ServiceSerializer(ModelSerializer):
    """Serializes Service objects from django model to JSON."""

    class Meta:
        """ServiceSerializer metadata."""
        model = Service
        fields = "__all__"


class AlertSerializer(ModelSerializer):
    """Serializes Alert objects from django model to JSON."""

    class Meta:
        """ServiceSerializer metadata."""
        model = Alert
        fields = "__all__"

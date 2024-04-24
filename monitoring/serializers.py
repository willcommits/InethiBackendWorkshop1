from rest_framework.serializers import ModelSerializer

from .models import NetworkDevice, Service


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

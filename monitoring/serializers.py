from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, SerializerMethodField
from dynamic_fields.serializers import DynamicFieldsModelSerializer

from . import models


class MeshSerializer(ModelSerializer):
    """Serializes Mesh objects from django model to JSON."""

    class Meta:
        """MeshSerializer metadata."""
        model = models.Mesh
        fields = "__all__"


class NodeSerializer(DynamicFieldsModelSerializer):
    """Serializes Node objects from django model to JSON."""

    class Meta:
        """Node metadata."""
        model = models.Node
        fields = "__all__"

    neighbours = PrimaryKeyRelatedField(many=True, read_only=True)
    status = SerializerMethodField()
    last_contact = SerializerMethodField()

    def get_status(self, node):
        return node.status.value
    
    def get_last_contact(self, node):
        return node.last_contact


class UnknownNodeSerializer(ModelSerializer):
    """Serializes UnknownNode objects from django model to JSON."""

    class Meta:
        """UnknownNodeSerializer metadata."""
        model = models.UnknownNode
        fields = "__all__"


class ServiceSerializer(ModelSerializer):
    """Serializes Service objects from django model to JSON."""

    class Meta:
        """ServiceSerializer metadata."""
        model = models.Service
        fields = "__all__"


class AlertSerializer(ModelSerializer):
    """Serializes Alert objects from django model to JSON."""

    class Meta:
        """ServiceSerializer metadata."""
        model = models.Alert
        fields = "__all__"

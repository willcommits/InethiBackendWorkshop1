from rest_framework.serializers import ModelSerializer, SerializerMethodField

from . import models


class MeshSerializer(ModelSerializer):
    """Serializes Mesh objects from django model to JSON."""

    class Meta:
        """MeshSerializer metadata."""
        model = models.Mesh
        fields = "__all__"


class NodeSerializer(ModelSerializer):
    """Serializes Node objects from django model to JSON."""

    memory_usage = SerializerMethodField()

    class Meta:
        """NodeSerializer metadata."""
        model = models.Node
        fields = "__all__"

    def get_memory_usage(self, ap: models.Ap) -> float:
        load = ap.nodeload_set.first()
        return load.mem_free / load.mem_total


class ApSerializer(ModelSerializer):
    """Serializes Access Point objects from django model to JSON."""

    memory_usage = SerializerMethodField()

    class Meta:
        """ApSerializer metadata."""
        model = models.Ap
        fields = "__all__"

    def get_memory_usage(self, ap: models.Ap) -> float:
        load = ap.apload_set.first()
        return load.mem_free / load.mem_total

class UnknownNodeSerializer(ModelSerializer):
    """Serializes UnknownNode objects from django model to JSON."""

    class Meta:
        """UnknownNodeSerializer metadata."""
        model = models.UnknownNode
        fields = "__all__"

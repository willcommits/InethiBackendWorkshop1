from rest_framework.serializers import ModelSerializer, SerializerMethodField
from dynamic_fields.serializers import DynamicFieldsModelSerializer

from . import models


class NodeUptmHistorySerializer(ModelSerializer):
    """Serializes node uptime histories from django model to JSON."""

    class Meta:
        """NodeUptmHistorySerializer metadata."""
        model = models.NodeUptmHistory
        fields = "__all__"


class ApUptmHistorySerializer(ModelSerializer):
    """Serializes AP uptime histories from django model to JSON."""

    class Meta:
        """ApUptmHistorySerializer metadata."""
        model = models.ApUptmHistory
        fields = "__all__"


class ApStationSerializer(ModelSerializer):
    """Serializes AP stations from django model to JSON."""

    class Meta:
        """ApStationSerializer metadata."""
        model = models.ApStation
        fields = "__all__"


class NodeStationSerializer(ModelSerializer):
    """Serializes Node stations from django model to JSON."""

    class Meta:
        """NodeStationSerializer metadata."""
        model = models.NodeStation
        fields = "__all__"


class MeshSerializer(ModelSerializer):
    """Serializes Mesh objects from django model to JSON."""

    class Meta:
        """MeshSerializer metadata."""
        model = models.Mesh
        fields = "__all__"


class NodeSerializer(DynamicFieldsModelSerializer):
    """Serializes Node objects from django model to JSON."""

    memory_usage = SerializerMethodField()
    nodeuptmhistory_set = NodeUptmHistorySerializer(many=True, read_only=True)
    nodestation_set = NodeStationSerializer(many=True, read_only=True)

    class Meta:
        """NodeSerializer metadata."""
        model = models.Node
        fields = "__all__"

    def get_memory_usage(self, ap: models.Ap) -> float:
        load = ap.nodeload_set.first()
        if not load:
            return -1.0
        return load.mem_free / load.mem_total


class ApSerializer(DynamicFieldsModelSerializer):
    """Serializes Access Point objects from django model to JSON."""

    memory_usage = SerializerMethodField()
    apuptmhistory_set = ApUptmHistorySerializer(many=True, read_only=True)
    apstation_set = ApStationSerializer(many=True, read_only=True)

    class Meta:
        """ApSerializer metadata."""
        model = models.Ap
        fields = "__all__"

    def get_memory_usage(self, ap: models.Ap) -> float:
        load = ap.apload_set.first()
        if not load:
            return -1.0
        return load.mem_free / load.mem_total

class UnknownNodeSerializer(ModelSerializer):
    """Serializes UnknownNode objects from django model to JSON."""

    class Meta:
        """UnknownNodeSerializer metadata."""
        model = models.UnknownNode
        fields = "__all__"

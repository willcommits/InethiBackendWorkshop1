from rest_framework.serializers import ModelSerializer, SerializerMethodField
from dynamic_fields.serializers import DynamicFieldsModelSerializer

from .models import Node, Service, Alert, UptimeMetric, NodeStation, Mesh, UnknownNode


class MeshSerializer(ModelSerializer):
    """Serializes Mesh objects from django model to JSON."""

    class Meta:
        """MeshSerializer metadata."""
        model = Mesh
        fields = "__all__"


class UptimeMetricSerializer(ModelSerializer):
    """Serializes node uptime histories from django model to JSON."""

    class Meta:
        """UptimeMetricSerializer metadata."""
        model = UptimeMetric
        fields = "__all__"


class NodeStationSerializer(ModelSerializer):
    """Serializes node stations from django model to JSON."""

    class Meta:
        """NodeStationSerializer metadata."""
        model = NodeStation
        fields = "__all__"


class NodeSerializer(DynamicFieldsModelSerializer):
    """Serializes Node objects from django model to JSON."""

    class Meta:
        """Node metadata."""
        model = Node
        fields = "__all__"

    memory_usage = SerializerMethodField()
    uptime_metrics = UptimeMetricSerializer(many=True, read_only=True)
    stations = NodeStationSerializer(many=True, read_only=True)

    def get_memory_usage(self, node: Node) -> float:
        load = node.loads.first()
        if not load:
            return -1.0
        return load.mem_free / load.mem_total


class UnknownNodeSerializer(ModelSerializer):
    """Serializes UnknownNode objects from django model to JSON."""

    class Meta:
        """UnknownNodeSerializer metadata."""
        model = UnknownNode
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

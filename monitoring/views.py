
from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers


class NodeViewSet(ModelViewSet):
    """View/Edit/Add/Delete Node items."""

    queryset = models.Node.objects.all()
    serializer_class = serializers.NodeSerializer


class ServiceViewSet(ModelViewSet):
    """View/Edit/Add/Delete Service items."""

    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer


class AlertsViewSet(ModelViewSet):
    """View/Edit/Add/Delete Alert items."""

    queryset = models.Alert.objects.all()
    serializer_class = serializers.AlertSerializer

class MeshViewSet(ModelViewSet):
    """View/Edit/Add/Delete Mesh items."""

    queryset = models.Mesh.objects.all()
    serializer_class = serializers.MeshSerializer


class UnknownNodeViewSet(ModelViewSet):
    """View/Edit/Add/Delete UnknownNode items."""

    queryset = models.UnknownNode.objects.all()
    serializer_class = serializers.UnknownNodeSerializer
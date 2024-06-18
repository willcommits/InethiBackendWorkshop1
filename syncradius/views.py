from rest_framework.viewsets import ModelViewSet
from dynamic_fields.mixins import DynamicFieldsViewMixin

from . import models
from . import serializers


class MeshViewSet(ModelViewSet):
    """View/Edit/Add/Delete Mesh items."""

    queryset = models.Mesh.objects.all()
    serializer_class = serializers.MeshSerializer


class NodeViewSet(DynamicFieldsViewMixin, ModelViewSet):
    """View/Edit/Add/Delete Node items."""

    queryset = models.Node.objects.all()
    serializer_class = serializers.NodeSerializer


class UnknownNodeViewSet(ModelViewSet):
    """View/Edit/Add/Delete UnknownNode items."""

    queryset = models.UnknownNode.objects.all()
    serializer_class = serializers.UnknownNodeSerializer


class ApViewSet(DynamicFieldsViewMixin, ModelViewSet):
    """View/Edit/Add/Delete AP items."""

    queryset = models.Ap.objects.all()
    serializer_class = serializers.ApSerializer

from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers


class UptimeViewSet(ModelViewSet):
    """View/Edit/Add/Delete UptimeMetric items."""

    queryset = models.UptimeMetric.objects.all()
    serializer_class = serializers.UptimeMetricSerializer


class FailuresViewSet(ModelViewSet):
    """View/Edit/Add/Delete FailuresMetric items."""

    queryset = models.FailuresMetric.objects.all()
    serializer_class = serializers.FailuresMetricSerializer


class RTTViewSet(ModelViewSet):
    """View/Edit/Add/Delete RTTMetric items."""

    queryset = models.RTTMetric.objects.all()
    serializer_class = serializers.RTTMetricSerializer


class ResourcesViewSet(ModelViewSet):
    """View/Edit/Add/Delete ResourcesMetric items."""

    queryset = models.ResourcesMetric.objects.all()
    serializer_class = serializers.ResourcesMetricSerializer


class DataUsageViewSet(ModelViewSet):
    """View/Edit/Add/Delete DataUsageMetric items."""

    queryset = models.DataUsageMetric.objects.all()
    serializer_class = serializers.DataUsageMetricSerializer

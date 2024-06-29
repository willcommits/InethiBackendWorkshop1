import enum
from datetime import datetime, timedelta
from django.utils import timezone
from django.db import models

from metrics.models import UptimeMetric


class Mesh(models.Model):
    """Mesh consisting of nodes."""

    name = models.CharField(max_length=128, primary_key=True)
    ssid = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now_add=True)


class Node(models.Model):
    """Database table for network devices."""

    class Status(enum.Enum):

        UNKNOWN = "Unknown"
        INACTIVE = "Inactive"
        UNREACHABLE = "Unreachable"
        OK = "Ok"

    # Required Fields
    mac = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    mesh = models.ForeignKey(Mesh, on_delete=models.CASCADE)
    # Optional Fields
    neighbours = models.ManyToManyField("Node", blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    hardware = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def status(self) -> Status:
        """Node status, based of the last uptime metric."""
        last_uptime_metric = UptimeMetric.objects.filter(mac=self.mac).order_by("-created").first()
        now = timezone.now()
        if last_uptime_metric is None:
            return Node.Status.UNKNOWN
        # TODO: Make this configurable
        elif (now - last_uptime_metric.created) > timedelta(days=1):
            return Node.Status.INACTIVE
        elif not last_uptime_metric.reachable:
            return Node.Status.UNREACHABLE
        return Node.Status.OK

    @property
    def last_contact(self) -> datetime | None:
        """Datetime of last contact."""
        last_uptime_metric = UptimeMetric.objects.filter(mac=self.mac).filter(reachable=True).order_by("-created").first()
        if last_uptime_metric is None:
            return None
        return last_uptime_metric.created

    def __str__(self):
        return f"Node {self.name} ({self.mac})"


class UnknownNode(models.Model):
    """Nodes that haven't been adopted yet."""

    mac = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    ip = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Unknown Node {self.mac} [{self.created}]"


class Service(models.Model):
    """Database table for services."""

    SERVICE_TYPES = (
        ("utility", "Utility"),
        ("entertainment", "Entertainment"),
        ("games", "Games"),
        ("education", "Education"),
    )

    API_LOCATIONS = (("cloud", "Cloud"), ("local", "Local"))

    url = models.URLField(max_length=100, unique=True)
    name = models.CharField(max_length=20, unique=True)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    api_location = models.CharField(max_length=10, choices=API_LOCATIONS)


class Alert(models.Model):
    """Alert sent to network managers."""

    ALERT_CATEGORIES = (
        ("node_down", "Node Down"),
        ("node_up", "Node Up"),
        ("unknown", "Unknown"),
    )

    ALERT_TYPES = (
        ("error", "Error"),
        ("warning", "Warning"),
        ("info", "Info"),
        ("success", "Success"),
    )

    category = models.CharField(max_length=20, choices=ALERT_CATEGORIES)
    type = models.CharField(max_length=10, choices=ALERT_TYPES)
    text = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

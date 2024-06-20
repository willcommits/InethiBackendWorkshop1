from django.db import models


class Cloud(models.Model):

    name = models.CharField(max_length=64, primary_key=True)
    description = models.CharField(max_length=255)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    created = models.DateTimeField()


class Mesh(models.Model):

    name = models.CharField(max_length=128, primary_key=True)
    ssid = models.CharField(max_length=32)
    cloud = models.ForeignKey(Cloud, on_delete=models.SET_NULL, blank=True, null=True)
    created = models.DateTimeField()


class Node(models.Model):
    """Database table for network devices."""

    DEVICE_TYPES = (
        ("switch", "Switch"),
        ("access_point", "Access Point"),
        ("firewall", "Firewall"),
        ("local_server", "Local Server"),
        ("dns_server", "DNS Server"),
        ("global_server", "Global Server"),
    )

    mesh = models.ForeignKey(Mesh, on_delete=models.SET_NULL, blank=True, null=True)
    neighbours = models.ManyToManyField("Node")
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    mac = models.CharField(max_length=255, primary_key=True)
    hardware = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    last_contact = models.DateTimeField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    created = models.DateTimeField()
    config_fetched = models.DateTimeField(blank=True, null=True)
    last_contact_from_ip = models.CharField(max_length=30)

    def __str__(self):
        return f"Node {self.name} ({self.mac})"


class NodeStation(models.Model):

    node = models.ForeignKey(
        Node, on_delete=models.SET_NULL, blank=True, null=True, related_name="stations"
    )
    radio_number = models.IntegerField()
    frequency_band = models.CharField(max_length=10, blank=True, null=True)
    mac = models.CharField(max_length=17)
    tx_bytes = models.BigIntegerField()
    rx_bytes = models.BigIntegerField()
    tx_packets = models.BigIntegerField()
    rx_packets = models.BigIntegerField()
    tx_bitrate = models.IntegerField()
    rx_bitrate = models.IntegerField()
    tx_failed = models.IntegerField()
    tx_retries = models.IntegerField()
    signal_now = models.IntegerField()
    signal_avg = models.IntegerField()
    created = models.DateTimeField()

    def __str__(self):
        return f"Node Station {self.node.name}: (R:{self.radio_number}-band:{self.frequency_band}) [{self.created}]"


class NodeLoad(models.Model):

    node = models.ForeignKey(
        Node, on_delete=models.SET_NULL, blank=True, null=True, related_name="loads"
    )
    mem_total = models.IntegerField(blank=True, null=True)
    mem_free = models.IntegerField(blank=True, null=True)
    uptime = models.CharField(max_length=255, blank=True, null=True)
    system_time = models.CharField(max_length=255)
    created = models.DateTimeField()

    def __str__(self):
        return (
            f"Node Load {self.node.name}: "
            f"Uptime: {self.uptime} "
            f"Memory: {self.mem_free / self.mem_total * 100:.0f}% "
            f"[{self.created}]"
        )


class UptimeMetric(models.Model):

    node = models.ForeignKey(
        Node,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="uptime_metrics",
    )
    reachable = models.BooleanField()
    loss = models.IntegerField()
    rtt_min = models.FloatField(null=True, blank=True)
    rtt_avg = models.FloatField(null=True, blank=True)
    rtt_max = models.FloatField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Node Uptime {self.node.name}: {'UP' if self.reachable else 'DOWN'} [{self.created}]"


class UnknownNode(models.Model):

    mac = models.CharField(max_length=255, primary_key=True)
    vendor = models.CharField(max_length=255, blank=True, null=True)
    from_ip = models.CharField(max_length=15)
    gateway = models.IntegerField()
    last_contact = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"Unknown Node {self.mac} [{self.last_contact}]"


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
    created_time = models.DateTimeField(auto_now_add=True)

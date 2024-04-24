from django.db import models


class NetworkDevice(models.Model):
    """Database table for network devices."""

    DEVICE_TYPES = (
        ('switch', 'Switch'),
        ('access_point', 'Access Point'),
        ('firewall', 'Firewall'),
        ('local_server', 'Local Server'),
        ('dns_server', 'DNS Server'),
        ('global_server', 'Global Server')
    )

    name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=20, choices=DEVICE_TYPES)
    ip_address = models.GenericIPAddressField(unique=True)

    def __str__(self):
        return f"{self.name} ({self.device_type})"


class Service(models.Model):
    """Database table for services."""

    SERVICE_TYPES = (
        ('utility', 'Utility'),
        ('entertainment', 'Entertainment'),
        ('games', 'Games'),
        ('education', 'Education')
    )

    API_LOCATIONS = (
        ('cloud', 'Cloud'),
        ('local', 'Local')
    )

    url = models.URLField(max_length=100, unique=True)
    name = models.CharField(max_length=20, unique=True)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    api_location = models.CharField(max_length=10, choices=API_LOCATIONS)

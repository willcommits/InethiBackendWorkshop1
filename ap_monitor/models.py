from django.db import models


class NetworkDevice(models.Model):
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

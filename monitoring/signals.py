import yaml
import requests
from requests.auth import HTTPBasicAuth

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings

from .models import NetworkDevice


def reload_prometheus():
    """Reload prometheus configuration."""
    username = settings.PROMETHEUS_USERNAME
    password = settings.PROMETHEUS_PASSWORD
    url = settings.PROMETHEUS_URL
    # response = requests.post(url, auth=HTTPBasicAuth(username, password))
    print(f"Reloaded Prometheus")

def sync_prometheus_data_to_yml():
    """Sync the IP addresses currently in the database to YAML config."""
    ip_addresses = NetworkDevice.objects.values_list("ip_address", flat=True)
    prometheus_path = settings.BASE_DIR / 'prometheus.yml'

    with open(prometheus_path, 'r', encoding="utf-8") as prometheus_file:
        prometheus_data = yaml.safe_load(prometheus_file)

    # Find the 'blackbox' job, append new IPs to its targets while avoiding duplicates
    for job in prometheus_data.get('scrape_configs', []):
        if job['job_name'] == 'blackbox':
            current_targets = set(job['static_configs'][0]['targets'] or [])
            updated_targets = current_targets.union(ip_addresses)
            job['static_configs'][0]['targets'] = list(updated_targets)
            break

    with open(prometheus_path, 'w', encoding="utf-8") as file:
        yaml.dump(prometheus_data, file, sort_keys=False)


@receiver(post_save, sender=NetworkDevice)
def update_prometheus_targets(sender, **kwargs):
    """Update prometheus targets when network devices are added or modified."""
    sync_prometheus_data_to_yml()
    reload_prometheus()


@receiver(post_delete, sender=NetworkDevice)
def remove_prometheus_targets(**kwargs):
    """Update prometheus targets when network devices are deleted."""
    sync_prometheus_data_to_yml()
    reload_prometheus()

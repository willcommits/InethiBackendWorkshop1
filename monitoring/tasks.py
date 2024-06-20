from celery import shared_task
from celery.utils.log import get_task_logger

from .models import Node, UptimeMetric
from .ping import ping

logger = get_task_logger(__name__)


@shared_task
def run_pings():
    for device in Node.objects.filter(last_contact_from_ip__isnull=False):
        ping_data = ping(device.last_contact_from_ip)
        UptimeMetric.objects.create(node=device, **ping_data)
        logger.info(f"PING {device.last_contact_from_ip}")

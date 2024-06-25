from celery import shared_task
from celery.utils.log import get_task_logger

from .sync.radiusdesk import run as syncrd

logger = get_task_logger(__name__)


@shared_task
def run_syncrd():
    logger.info("Syncing with radiusdesk")
    syncrd()

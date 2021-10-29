from celery import shared_task
from datetime import datetime, timedelta
from api.models import Url

@shared_task(name="deregister_urls")
def dereg_urls():
    """ Get the time delta """
    time_delta = datetime.now() - timedelta(minutes=1)

    """ Query for expired URLs """
    expired_urls = Url.objects.filter(url_last_click__lt=time_delta)

    if expired_urls.exists():
        for url in expired_urls:
            url.mark_expired()
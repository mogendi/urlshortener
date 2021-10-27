import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling  # noqa


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urlshortener.settings')

application = Cling(get_wsgi_application())
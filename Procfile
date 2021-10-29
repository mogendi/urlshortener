web: gunicorn urlshortener.wsgi
worker: celery -A urlshortener worker
beat: celery -A urlshortener beat
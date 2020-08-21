import os
from celery import Celery
from decouple import config

enviroment = config('ENVIRONMENT', 'dev')

if enviroment.lower() == 'production' or enviroment.lower() == 'staging':
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        'di_website.settings.production')
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'di_website.settings.dev')

app = Celery('di_website')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

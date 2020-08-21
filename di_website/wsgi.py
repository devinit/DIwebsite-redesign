"""
WSGI config for di_website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from decouple import config

enviroment = config('ENVIRONMENT', 'dev')

if enviroment.lower() == 'production' or enviroment.lower() == 'staging':
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        'di_website.settings.production')
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'di_website.settings.dev')

application = get_wsgi_application()

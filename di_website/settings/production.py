from .base import *
from decouple import config

DEBUG = False

SECRET_KEY = config('SECRET_KEY', '3bxacdim+p6h*6-j7(zq$t4#4=vzu97+xzeb9-=0rqbh+_o#_d')
ALLOWED_HOSTS = ['127.0.0.1', '159.65.56.142', 'localhost', 'devinit.org', 'www.devinit.org']

try:
    from .local import *
except ImportError:
    pass

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'null': {
            'class': 'logging.NullHandler',
        },
    },
    'loggers': {
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
    },
}

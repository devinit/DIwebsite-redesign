from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3bxacdim+p6h*6-j7(zq$t4#4=vzu97+xzeb9-=0rqbh+_o#_d'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = os.getenv('EMAIL_BACKEND') or 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS+[
    'debug_toolbar',
]
try:
    from .local import *
except ImportError:
    pass

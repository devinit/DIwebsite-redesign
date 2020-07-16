from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3bxacdim+p6h*6-j7(zq$t4#4=vzu97+xzeb9-=0rqbh+_o#_d'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

try:
    from .local import *
except ImportError:
    pass

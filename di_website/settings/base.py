"""
Django settings for di_website project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
from decouple import config
import dotenv

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

ADMINS = [
    ('Edwin', 'edwin.magezi@devinit.org'),
    ('Alex', 'alex.miller@devinit.org'),
    ('David', 'david.ebukali@devinit.org')
]


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'di_website.footnotes',
    'di_website.home',
    'di_website.users',
    'di_website.search',
    'di_website.ourteam',
    'di_website.common',
    'di_website.vacancies',
    'di_website.blog',
    'di_website.news',
    'di_website.events',
    'di_website.place',
    'di_website.contactus',
    'di_website.about',
    'di_website.general',
    'di_website.project',
    'di_website.whatwedo',
    'di_website.publications',
    'di_website.downloads',
    'di_website.workforus',
    'di_website.datasection',
    'di_website.api',

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.contrib.settings',
    'wagtail.contrib.styleguide',
    'wagtail.contrib.table_block',
    'wagtail.contrib.search_promotions',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'wagtaillinkchecker',
    'wagtailgeowidget',

    'modelcluster',
    'taggit',
    'wagtailfontawesome',
    'widget_tweaks',
    'wagtailmetadata',

    'django.contrib.sitemaps',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'di_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'di_website.context.globals',
            ],
        },
    },
]

WSGI_APPLICATION = 'di_website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

dotenv.read_dotenv('.env')

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

if config('ELASTIC_SEARCH_URL', ''):

    elastic_search_tokens = [
        'letter',
        'digit',
        'whitespace'
    ]

    WAGTAILSEARCH_BACKENDS = {
        'default': {
            'BACKEND': 'wagtail.search.backends.elasticsearch6',
            'AUTO_UPDATE': False,
            'ATOMIC_REBUILD': True,
            'URLS': [config('ELASTIC_SEARCH_URL', '')],
            'TIMEOUT': 10,
            'INDEX_SETTINGS': {
                'settings': {
                    'analysis': {
                        'tokenizer': {
                            'ngram_tokenizer': {
                                'type': 'nGram',
                                'min_gram': 3,
                                'max_gram': 10,
                                'token_cars': elastic_search_tokens
                            },
                            'edgengram_tokenizer': {
                                'type': 'edgeNGram',
                                'min_gram': 1,
                                'max_gram': 10,
                                'side': 'front',
                                'token_cars': elastic_search_tokens
                            }
                        },
                        'filter': {
                            'ngram': {
                                'type': 'nGram',
                                'min_gram': 3,
                                'max_gram': 10
                            },
                            'edgengram': {
                                'type': 'edgeNGram',
                                'min_gram': 1,
                                'max_gram': 10
                            }
                        },
                        'index': {
                            'number_of_shards': 2
                        }

                    }
                }
            }
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'patterns/converted-html/assets'),
    os.path.join(BASE_DIR, 'di_website/static'),
]

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# Javascript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/2.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
STATIC_URL = '/assets/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'storage')
MEDIA_URL = '/media/'


# Wagtail settings

WAGTAIL_SITE_NAME = "di_website"

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = os.getenv('BASE_URL') or 'http://devinit.org'

INTERNAL_IPS = ["127.0.0.1"]

# Email settings

EMAIL_BACKEND = os.getenv('EMAIL_BACKEND') or 'django.core.mail.backends.console.EmailBackend'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL') or 'devinitautomailer@gmail.com'
SERVER_EMAIL = DEFAULT_FROM_EMAIL

# hubspot settings
HS_API_KEY = config('HS_API_KEY', default='')
HS_TICKET_PIPELINE = config('HS_TICKET_PIPELINE', '891429')
HS_TICKET_PIPELINE_STAGE = config('HS_TICKET_PIPELINE_STAGE', '891430')

GOOGLE_MAPS_V3_APIKEY = "AIzaSyAZAIjZtkBlsF0ZqvrlkvyLfVn6Bju6bJ4"

# Celery
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')

# Disable update notifications on CMS
WAGTAIL_ENABLE_UPDATE_CHECK = False

# Fix for max fields error message
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000

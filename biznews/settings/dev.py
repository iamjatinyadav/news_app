from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']
DEV = DEBUG

INSTALLED_APPS += ('debug_toolbar',)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbbiznews',
        'USER': 'postgres',
        'PASSWORD': 'abcd1234',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

SECRET_KEY = 'devel'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SITE_ID = 2

AUTH_PASSWORD_VALIDATORS = []

INTERNAL_IPS = ("127.0.0.1",)



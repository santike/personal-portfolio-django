from .base import *

DEBUG = True

ALLOWED_HOSTS = ['.herokuapp.com'] # depende del lugar en produccion

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER' :'',
        'PASSWORD':'',
        'HOST': '',
        'PORT': 5432,
    }
}
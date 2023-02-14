"""
WSGI config for django_portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_portfolio.settings.local')

application = get_wsgi_application()

"""
ver This is a simple Django middleware utility that allows you to properly serve static assets from production with a WSGI server like Gunicorn.

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/

from dj_static import Cling
application = Cling(get_wsgi_application())
"""
"""
WSGI config for django_test project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append('/home/gk/django_test')
sys.path.append('/home/gk/django_test/django_test')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_test.settings")

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

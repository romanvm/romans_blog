"""
WSGI config for romans_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dotenv import read_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

read_dotenv(os.path.join(BASE_DIR, '.env'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "romans_blog.settings.dev")

application = get_wsgi_application()

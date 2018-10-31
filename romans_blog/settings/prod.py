# (c) 2018, Roman Miroshnychenko <roman1972@gmail.com>
# License: GPL v.3

from django.core.exceptions import ImproperlyConfigured
from dotenv import read_dotenv
from .base import *

read_dotenv(os.path.join(BASE_DIR, '.env'))

SECURE_SSL_REDIRECT = True

try:
    DEBUG = os.getenv('DEBUG') == 'true'
    SECRET_KEY = os.environ['SECRET_KEY']
    ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'].split(',')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['DB_NAME'],
            'USER': os.environ['DB_USER'],
            'PASSWORD': os.environ['DB_PASS'],
            'HOST': os.environ['DB_HOST'],
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            }
        }
    }
except KeyError as ex:
    raise ImproperlyConfigured('Env variable {} is not set!'.format(ex)) from ex

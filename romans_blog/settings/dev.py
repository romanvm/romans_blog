# (c) 2018, Roman Miroshnychenko <roman1972@gmail.com>
# License: GPL v.3

from .base import *

# INSTALLED_APPS.insert(-8, 'debug_toolbar')

# MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

INTERNAL_IPS = ['127.0.0.1']

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('DB_NAME') or 'romans_blog',
            'USER': os.getenv('DB_USER') or 'developer',
            'PASSWORD': os.getenv('DB_PASS') or '',
            'HOST': os.getenv('DB_HOST') or 'localhost',
            'OPTIONS': {
                'charset': 'utf8',
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                'isolation_level': 'read committed'
            },
            'TEST': {
                'CHARSET': 'utf8',
                'COLLATION': 'utf8_general_ci;'
            }
        }
    }

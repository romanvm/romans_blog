# (c) 2018, Roman Miroshnychenko <roman1972@gmail.com>
# License: GPL v.3

from .base import *

INSTALLED_APPS.insert(-8, 'debug_toolbar')

MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

INTERNAL_IPS = ['127.0.0.1']

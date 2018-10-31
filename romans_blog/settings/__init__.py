# (c) 2018, Roman Miroshnychenko <roman1972@gmail.com>
# License: GPL v.3

# Necessary for imports inside base.py to work properly
SECRET_KEY = 'dummy'
STATIC_URL = '/static/'

from .dev import *

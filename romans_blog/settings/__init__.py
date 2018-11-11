# (c) 2018, Roman Miroshnychenko <roman1972@gmail.com>
# License: GPL v.3

# Necessary for imports inside base.py to work properly
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
SECRET_KEY = 'dummy'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


from .dev import *

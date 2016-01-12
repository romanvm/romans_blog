#!/usr/bin/env python3
# coding: utf-8
# Module: update_index
# Created on: 12.01.2016
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)
"""
Update haystack index on pythonanywhere.com
"""

import os
import sys
import subprocess

# Change this to your actual virtual environment
VENV = os.path.join(os.path.expandvars('$HOME'), 'venv')
activate = os.path.join(VENV, 'bin', 'activate_this.py')
with open(activate, 'r') as fo:
    exec(fo.read(), dict(__file__=activate))
path = os.path.join(os.path.expandvars('$HOME'), 'romans_blog')
if path not in sys.path:
    sys.path.insert(0, path)
subprocess.call(['python', 'manage.py', 'update_index'])

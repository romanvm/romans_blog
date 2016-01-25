#!/usr/bin/python3.4
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

home = os.path.expandvars('$HOME')
# Change this to your actual virtual environment
venv = os.path.join(home, 'venv')
activate = os.path.join(venv, 'bin', 'activate_this.py')
with open(activate, 'r') as fo:
    exec(fo.read(), dict(__file__=activate))
path = os.path.join(home, 'romans_blog')
if path not in sys.path:
    sys.path.insert(0, path)
os.chdir(path)
subprocess.call(['python', 'manage.py', 'update_index'])

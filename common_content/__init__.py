# coding: utf-8
# Author: Roman Miroshnychenko aka Roman V.M.
# E-mail: romanvm@yandex.ua
"""
This package contains common content used by all applications
"""

from django.contrib.staticfiles.storage import staticfiles_storage

__all__ = ['base_url']

base_url = staticfiles_storage.url('common_content/')

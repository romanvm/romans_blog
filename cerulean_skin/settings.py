# coding: utf-8
# Module: settings
# Created on: 20.12.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)
"""
Contains the variables defining specific style classes for TinyMCE editor
"""

import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Image styles for TinyMCE 4
IMAGE_CLASS_LIST = [
    {'title': 'Responsive', 'value': 'img-responsive'},
    {'title': 'Rounded', 'value': 'img-responsive img-rounded'},
    {'title': 'Thumbnail', 'value': 'img-responsive img-thumbnail'},
    {'title': 'Circle', 'value': 'img-responsive img-circle'},
]
# Table styles for TinyMCE 4
TABLE_CLASS_LIST = [
    {'title': 'Simple', 'value': 'table'},
    {'title': 'Bordered', 'value': 'table table-bordered'},
    {'title': 'Striped', 'value': 'table table-striped'},
    {'title': 'Condensed', 'value': 'table table-condensed'},
]
# Table row styles for TinyMCE 4
TABLE_ROW_CLASS_LIST = [
    {'title': 'None', 'value': ''},
    {'title': 'Green', 'value': 'success'},
    {'title': 'Red', 'value': 'danger'},
    {'title': 'Blue', 'value': 'info'},
]

if settings.DEBUG:
    storage = FileSystemStorage(location=os.path.join(os.path.dirname(__file__), 'static'))
else:
    storage = FileSystemStorage(location=settings.STATIC_ROOT)
# Content styles for TinyMCE 4
CSS = ('cerulean_skin/css/bootstrap.min.css', 'cerulean_skin/css/cerulean_skin.css')
content_style = ''
for css in CSS:
    with storage.open(css) as file_obj:
        content_style += file_obj.read().decode('utf-8')

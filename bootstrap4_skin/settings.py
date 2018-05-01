# coding: utf-8
# Module: settings
# Author: Roman Miroshnychenko aka Roman V.M. (roman1972@gmail.com)
"""
Contains the variables defining specific style classes for TinyMCE editor
"""

from django.contrib.staticfiles.storage import staticfiles_storage

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
    # Translators: "None" means no styles for a table
    {'title': 'None', 'value': ''},
    {'title': 'Green', 'value': 'success'},
    {'title': 'Red', 'value': 'danger'},
    {'title': 'Blue', 'value': 'info'},
]

# Content styles for TinyMCE 4
CONTENT_CSS = [
    staticfiles_storage.url('cerulean_skin/css/bootstrap.min.css'),
    staticfiles_storage.url('cerulean_skin/css/font-awesome.min.css'),
    staticfiles_storage.url('cerulean_skin/css/cerulean_skin.css'),
]

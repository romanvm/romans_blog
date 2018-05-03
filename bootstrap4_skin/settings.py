# coding: utf-8
# Module: settings
# Author: Roman Miroshnychenko aka Roman V.M. (roman1972@gmail.com)
"""
Contains the variables defining specific style classes for TinyMCE editor
"""

from django.contrib.staticfiles.storage import staticfiles_storage

# Image styles for TinyMCE 4
IMAGE_CLASS_LIST = [
    {'title': 'Responsive', 'value': 'img-fluid'},
    {'title': 'Rounded', 'value': 'img-fluid rounded'},
    {'title': 'Thumbnail', 'value': 'img-fluid img-thumbnail'},
]
# Table styles for TinyMCE 4
TABLE_CLASS_LIST = [
    {'title': 'Simple', 'value': 'table'},
    {'title': 'Bordered', 'value': 'table table-bordered'},
    {'title': 'Striped', 'value': 'table table-striped'},
    {'title': 'Small', 'value': 'table table-sm'},
]
# Table row styles for TinyMCE 4
TABLE_ROW_CLASS_LIST = [
    # Translators: "None" means no styles for a table
    {'title': 'None', 'value': ''},
    {'title': 'Green', 'value': 'table-success'},
    {'title': 'Red', 'value': 'table-danger'},
    {'title': 'Blue', 'value': 'table-primary'},
]

# Content styles for TinyMCE 4
CONTENT_CSS = [
    staticfiles_storage.url('bootstrap4_skin/css/bootstrap.min.css'),
    staticfiles_storage.url('bootstrap4_skin/css/font-awesome-all.min.css'),
    staticfiles_storage.url('bootstrap4_skin/css/styles.css'),
]

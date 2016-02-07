# coding: utf-8
# Module: settings
# Created on: 20.12.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)
"""
Contains the variables defining specific style classes for TinyMCE editor
"""

from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils.translation import ugettext as _

# Image styles for TinyMCE 4
IMAGE_CLASS_LIST = [
    {'title': _('Responsive'), 'value': 'img-responsive'},
    {'title': _('Rounded'), 'value': 'img-responsive img-rounded'},
    {'title': _('Thumbnail'), 'value': 'img-responsive img-thumbnail'},
    {'title': _('Circle'), 'value': 'img-responsive img-circle'},
]
# Table styles for TinyMCE 4
TABLE_CLASS_LIST = [
    {'title': _('Simple'), 'value': 'table'},
    {'title': _('Bordered'), 'value': 'table table-bordered'},
    {'title': _('Striped'), 'value': 'table table-striped'},
    {'title': _('Condensed'), 'value': 'table table-condensed'},
]
# Table row styles for TinyMCE 4
TABLE_ROW_CLASS_LIST = [
    # Translators: "None" means no styles for a table
    {'title': _('None'), 'value': ''},
    {'title': _('Green'), 'value': 'success'},
    {'title': _('Red'), 'value': 'danger'},
    {'title': _('Blue'), 'value': 'info'},
]

# Content styles for TinyMCE 4
CONTENT_STYLE = [
    staticfiles_storage.url('cerulean_skin/css/bootstrap.min.css'),
    staticfiles_storage.url('cerulean_skin/css/font-awesome.min.css'),
    staticfiles_storage.url('cerulean_skin/css/cerulean_skin.css'),
    staticfiles_storage.url('cerulean_skin/css/prism.css'),
]

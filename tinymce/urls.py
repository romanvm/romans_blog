# Copyright (c) 2008 Joost Cassee
# Licensed under the terms of the MIT License (see LICENSE.txt)
from tinymce.views import textareas_js, spell_check, flatpages_link_list, compressor, filebrowser

try:
    from django.conf.urls import url
except:
    from django.conf.urls.defaults import url

urlpatterns = [
    url(r'^js/textareas/(?P<name>.+)/$', textareas_js, name='tinymce-js'),
    url(r'^js/textareas/(?P<name>.+)/(?P<lang>.*)$', textareas_js, name='tinymce-js-lang'),
    url(r'^spellchecker/$', spell_check, name='tinymce-spellchecker'),
    url(r'^flatpages_link_list/$', flatpages_link_list),
    url(r'^compressor/$', compressor, name='tinymce-compressor'),
    url(r'^filebrowser/$', filebrowser, name='tinymce-filebrowser'),
]

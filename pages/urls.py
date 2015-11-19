# coding: utf-8
# Module: urls
# Created on: 17.11.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from django.conf.urls import url
from .views import page_view

urlpatterns = [
    url(r'^$', page_view, name='page')
]

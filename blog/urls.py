# coding: utf-8
# Module: urls
# Created on: 17.11.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from django.conf.urls import url
from .views import blog_index_view

urlpatterns = [
    url(r'^$', blog_index_view, name='blog_index')
]

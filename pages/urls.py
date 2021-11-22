# coding: utf-8
# Module: urls
# Created on: 17.11.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from django.conf.urls import url

from .apps import PagesAppConfig
from .views import PageView

app_name = PagesAppConfig.name

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', PageView.as_view(), name='page')
]

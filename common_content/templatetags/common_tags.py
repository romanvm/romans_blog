# coding: utf-8
# Created on: 10.10.2016
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from django import template
from ..utils import get_site_config

register = template.Library()
register.simple_tag(get_site_config)

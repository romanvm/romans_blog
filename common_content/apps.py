# coding: utf-8
# Created on: 06.10.2017
# Author: Roman Miroshnychenko aka Roman V.M. (roman1972@gmail.com)


from django.apps.config import AppConfig
from django.utils.translation import ugettext_lazy as _


class CommonContentAppConfig(AppConfig):
    name = 'common_content'
    verbose_name = _('Common Content')

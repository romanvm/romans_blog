# coding: utf-8
# Module: sitemap
# Created on: 30.12.2015
# Author: Roman Miroshnychenko aka Roman V.M.
# E-mail: romanvm@yandex.ua

from django.contrib.sitemaps import Sitemap
from .models import MenuLink


class PagesSiteMap(Sitemap):
    changefreq = 'yearly'
    priority = 0.5

    def items(self):
        return MenuLink.objects.filter(page__isnull=False)

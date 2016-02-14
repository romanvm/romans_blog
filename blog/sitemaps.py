# coding: utf-8
# Module: sitemap
# Created on: 30.12.2015
# Author: Roman Miroshnychenko aka Roman V.M.
# E-mail: romanvm@yandex.ua

from django.contrib.sitemaps import Sitemap
from .models import Post


class BlogPostsSiteMap(Sitemap):
    changefreq = 'never'
    priority = 0.5

    def items(self):
        return Post.objects.published()

    def lastmod(self, obj):
        return obj.last_updated

# coding: utf-8
# Module: feeds
# Created on: 06.01.2016
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)
"""
Provides RSS and Atom feeds for recent Posts
"""

from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.conf import settings
from django.utils.translation import ugettext as _
from django.utils.text import Truncator
from .models import Post


class RecentPostsRSSFeed(Feed):
    title = _('{0} - Recent Posts').format(settings.SITE_NAME)
    link = '/'
    description = _('Recent posts from {0}').format(settings.SITE_NAME)

    def items(self):
        return Post.objects.published()[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return Truncator(item.content).words(50, html=True)


class RecentPostsAtomFeed(RecentPostsRSSFeed):
    feed_type = Atom1Feed

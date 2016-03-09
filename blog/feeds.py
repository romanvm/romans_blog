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
from .utils import post_truncator
from .models import Post


class RecentPostsRSSFeed(Feed):
    title = ' - '.join((settings.SITE_NAME, _('Recent Posts')))
    link = '/'
    description = _('Recent posts from {0}').format(settings.SITE_NAME)

    def items(self):
        return Post.objects.published()[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return post_truncator(item, '<em><a href="{0}">{1}</a></em>'.format(item.get_absolute_url(),
                                                                            _('Read more...')))


class RecentPostsAtomFeed(RecentPostsRSSFeed):
    feed_type = Atom1Feed

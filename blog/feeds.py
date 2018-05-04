# coding: utf-8
# Module: feeds
# Created on: 06.01.2016
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)
"""
Provides RSS and Atom feeds for recent Posts
"""

from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.utils.translation import ugettext as _
from common_content.utils import get_site_config
from .utils import post_truncator
from .models import Post


class RecentPostsRSSFeed(Feed):
    link = '/'

    def get_feed(self, obj, request):
        config = get_site_config()
        self.title = ' - '.join((config.site_name, _('Recent Posts')))
        self.description = _('Recent posts from {0}').format(config.site_name)
        return super().get_feed(obj, request)

    def items(self):
        return Post.objects.published()[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return post_truncator(item, '<em><a href="{0}">{1}</a></em>'.format(item.get_absolute_url(),
                                                                            _('Read more...')))


class RecentPostsAtomFeed(RecentPostsRSSFeed):
    feed_type = Atom1Feed

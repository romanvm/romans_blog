# coding: utf-8
# Module: feeds
# Created on: 06.01.2016
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)
"""
Provides RSS and Atom feeds for recent Posts
"""

from django.contrib.syndication.views import Feed
from django.conf import settings
from django.utils.text import Truncator
from .models import Post


class PostsRSSFeed(Feed):
    title = 'Roman\'s '

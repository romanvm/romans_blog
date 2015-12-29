# coding: utf-8
# Module: urls
# Created on: 17.11.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from django.conf.urls import url
from .views import (BlogHomeView, BlogPostView, BlogFeaturedPostsView,
                    BlogCategoryView, BlogCategoriesListView,
                    BlogArhiveView, BlogMonthArchiveView)

urlpatterns = [
    url(r'^post/(?P<slug>[\w-]+)-(?P<pk>\d+)/$', BlogPostView.as_view(), name='post'),
    url(r'^featured/$', BlogFeaturedPostsView.as_view(), name='featured_posts'),
    url(r'^categories/(?P<slug>[\w-]+)/$', BlogCategoryView.as_view(), name='category'),
    url(r'^categories/$', BlogCategoriesListView.as_view(), name='categories_list'),
    url(r'^archive/(?P<year>\d{4})-(?P<month>\d{1,2})/$', BlogMonthArchiveView.as_view(), name='month_archive'),
    url(r'^archive/$', BlogArhiveView.as_view(), name='archive'),
    url(r'^$', BlogHomeView.as_view(), name='home'),
]

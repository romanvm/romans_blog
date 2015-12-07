# coding: utf-8
# Module: urls
# Created on: 17.11.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from django.conf.urls import url
from .views import BlogHomeView, BlogPostView, BlogFeaturedPostsView, BlogCategoryView, BlogCategoriesListView

urlpatterns = [
    url(r'^post/(?P<slug>[\w-]+)-(?P<pk>\d+)/$', BlogPostView.as_view(), name='blog_post'),
    url(r'^featured/$', BlogFeaturedPostsView.as_view(), name='featured_posts'),
    url(r'^categories/(?P<slug>[\w-]+)/$', BlogCategoryView.as_view(), name='blog_category'),
    url(r'^categories/$', BlogCategoriesListView.as_view(), name='blog_categories_list'),
    url(r'^$', BlogHomeView.as_view(), name='blog_home'),
]

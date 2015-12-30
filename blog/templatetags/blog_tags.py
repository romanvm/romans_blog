# coding: utf-8
# Module: blog_tags
# Created on: 25.11.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from collections import namedtuple
from django import template
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext
from ..models import Category, Post

_ = ugettext
register = template.Library()
SideBarObjects = namedtuple('SideBarObjects', ['objects', 'more'])


@register.simple_tag
def get_site_name():
    """
    Get site name from settings
    """
    return settings.SITE_NAME


@register.simple_tag
def get_disqus_shortname():
    """
    Get Disqus shortname
    """
    return settings.DISQUS_SHORTNAME


@register.assignment_tag
def get_categories():
    return Category.objects.all()


@register.assignment_tag
def get_posts_digest(featured=False):
    """
    Get the lists of the latest posts (general of featured) for the blog sidebar
    """
    posts = Post.objects.filter(is_published=True)
    if featured:
        posts = posts.filter(is_featured=True)
        more_link = reverse('blog:featured_posts')
    else:
        more_link = reverse('blog:home')
    more = more_link if posts.count() > settings.BLOG_SIDEBAR_POSTS_COUNT else None
    return SideBarObjects(posts[:settings.BLOG_SIDEBAR_POSTS_COUNT], more)


@register.assignment_tag
def get_archive_digest():
    """
    Get the list of the most recent months from the blog archive for the blog sidebar
    """
    months = Post.objects.filter(is_published=True).dates('date_published', 'month', order='DESC')
    more = reverse('blog:archive') if months.count() > settings.BLOG_SIDEBAR_POSTS_COUNT else None
    return SideBarObjects(months[:settings.BLOG_SIDEBAR_MONTHS_COUNT], more)


@register.assignment_tag
def get_blog_menu_links():
    """
    Get blog menu links for the site main menu.
    """
    MenuLink = namedtuple('MenuLink', ['caption', 'url'])
    featured = Post.objects.filter(is_featured=True)
    featured_link = reverse('blog:featured_posts') if featured.count() else None
    return (
        MenuLink(_('Home'), reverse('blog:home')),
        MenuLink(_('Featured'), featured_link),
        MenuLink(_('Archive'), reverse('blog:archive'))
    )


@register.assignment_tag
def get_url(url_name, *args, **kwargs):
    """
    Get reverse URL as a template variable
    """
    return reverse(url_name, args=args, kwargs=kwargs)

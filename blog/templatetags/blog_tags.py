# coding: utf-8
# Module: blog_tags
# Created on: 25.11.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from collections import namedtuple
from django import template
from django.conf import settings
from django.core.urlresolvers import reverse
from ..models import Category, Post

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
    posts = Post.objects.filter(is_published=True)
    if featured:
        posts = posts.filter(is_featured=True)
    latest_posts = posts[:settings.BLOG_SIDEBAR_POSTS_COUNT]
    more = reverse('blog:blog_home') if posts.count() > settings.BLOG_SIDEBAR_POSTS_COUNT else None
    return SideBarObjects(latest_posts, more)


@register.tag(name='captureas')
def do_captureas(parser, token):
    """
    Allows to capture template tag output as a template variable.

    Example::

        {% captureas home_url %}{% url "blog:blog_home" %}{% endcaptureas %}
        <li class="{% if request.path == home_url %}active{% endif %}">
    """
    try:
        tag_name, args = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError("'captureas' node requires a variable name.")
    nodelist = parser.parse(('endcaptureas',))
    parser.delete_first_token()
    return CaptureasNode(nodelist, args)


class CaptureasNode(template.Node):
    def __init__(self, nodelist, varname):
        self.nodelist = nodelist
        self.varname = varname

    def render(self, context):
        output = self.nodelist.render(context)
        context[self.varname] = output
        return ''

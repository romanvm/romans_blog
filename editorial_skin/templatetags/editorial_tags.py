# coding: utf-8
# Created on: 06.10.2017
# Author: Roman Miroshnychenko aka Roman V.M. (roman1972@gmail.com)

from django import template
from django.utils.translation import ugettext as _
from django.utils.html import mark_safe
from blog.utils import post_truncator

register = template.Library()


@register.filter
@mark_safe
def render_post_categories(post):
    """
    Filter

    :param post: blog post
    :return: rendered comma-separated list of post categories enclosed in as <a> tags
    """
    categories = []
    for category in post.categories.all():
        categories.append('<a href="{url}">{name}</a>'.format(url=category.get_absolute_url(), name=category.name))
    return ',&nbsp;'.join(categories)


@register.filter
@mark_safe
def truncate_post(post):
    """
    Filter

    Truncate a Post text to a page separator.
    The separator is inserted by TinyMCE ``pagebreak`` plugin
    that is used to emulate "blog post cut" feature.

    Only the 1st separator is taken into account, other separators, if any,
    are ignored.

    :param post: blog post
    :return: properly terminated truncated post
    """
    return post_truncator(post, '&nbsp;(<em><a href="{0}">{1}</a></em>)'.format(post.get_absolute_url(),
                                                                                _('Read more...')))


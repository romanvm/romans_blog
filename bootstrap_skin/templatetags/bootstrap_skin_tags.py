# coding: utf-8
# Module: bootstrap_skin_tags
# Created on: 26.12.2015
# Author: Roman Miroshnychenko aka Roman V.M.
# E-mail: romanvm@yandex.ua

from django import template
from django.utils.text import Truncator

register = template.Library()


@register.filter
def render_post_categories(post):
    """
    Render the list of post categories as as <a> tags
    """
    categories = []
    for category in post.categories.all():
        categories.append('<a href="{url}">{name}</a>'.format(url=category.get_absolute_url(), name=category.name))
    return ',&nbsp;'.join(categories)


@register.filter
def truncate_post(post, words):
    """
    Truncate a Pots text to a given number of words.
    """
    terminator = '&nbsp;(<strong><a href="{0}">...</a></strong>)'.format(post.get_absolute_url())
    return Truncator(post.content).words(words, truncate=terminator, html=True)

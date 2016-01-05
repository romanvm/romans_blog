# coding: utf-8
# Module: paper_skin_tags
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
    Truncate a Post text to a given number of words.

    It takes into account the case when a truncated fragment may contain
    code snippets in ``<pre>`` blocks and properly terminates such fragment.
    """
    MARKER = '%{-#$*$#-}%'
    truncated = Truncator(post.content).words(words, truncate=MARKER, html=True)
    if MARKER in truncated:
        terminator = '&nbsp;(<strong><a href="{0}">...</a></strong>)'.format(post.get_absolute_url())
    else:
        terminator = ''
    truncated = truncated.replace(MARKER, '')
    if truncated[-6:] == '</pre>':
        tag = '<p>'
    else:
        truncated = truncated[:-4]
        tag = ''
    return '{trunc}{tag}{term}</p>'.format(trunc=truncated, tag=tag, term=terminator)

# coding: utf-8
# Module: cerulean_skin_tags
# Created on: 26.12.2015
# Author: Roman Miroshnychenko aka Roman V.M.
# E-mail: romanvm@yandex.ua

import re
from bs4 import BeautifulSoup
from django import template
from django.conf import settings

register = template.Library()


@register.filter
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
    separator = settings.TINYMCE_DEFAULT_CONFIG['pagebreak_separator']
    terminator = '(<strong><a href="{0}">...</a></strong>)'.format(post.get_absolute_url())
    post_parts = post.content.split(separator)
    if len(post_parts) > 1:
        truncated_html = post_parts[0]
        post_digest = BeautifulSoup(truncated_html, 'html.parser').prettify()
        end_tag = re.search(r'</\w+?>$', post_digest, re.UNICODE | re.IGNORECASE).group(0)
        if end_tag.lower() == '</p>':
            return post_digest[:-4] + terminator + '</p>'
        else:
            return post_digest + '<p>' + terminator + '</p>'
    else:
        return post.content

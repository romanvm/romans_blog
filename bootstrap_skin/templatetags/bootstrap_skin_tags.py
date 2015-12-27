# coding: utf-8
# Module: bootstrap_skin_tags
# Created on: 26.12.2015
# Author: Roman Miroshnychenko aka Roman V.M.
# E-mail: romanvm@yandex.ua

from django import template

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
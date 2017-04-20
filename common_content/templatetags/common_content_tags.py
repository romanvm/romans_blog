# coding: utf-8
# Created on: 10.10.2016
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from django import template
from django.conf import settings
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag
def get_site_name():
    """
    Simple tag

    :return: site name from settings
    """
    return settings.SITE_NAME


@register.simple_tag
def get_url(url_name, **kwargs):
    """
    Simple tag

    Get reverse URL as a template variable

    :param url_name: the name of a path from urls
    :return: relative URL path
    """
    return reverse(url_name, kwargs=kwargs)


@register.inclusion_tag('common_content/google_analytics.html', takes_context=False)
def render_google_analytics():
    """
    Inclusion tag

    Renders Google Analytics JS code

    If ``settings.GOOGLE_ANALYTICS_ID`` is empty, no code will be rendered.

    :return: rendered GA html code.
    """
    return {'google_analytics_id': settings.GOOGLE_ANALYTICS_ID}

# coding: utf-8
# Module: page_tags
# Created on: 19.11.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

import json
from django import template
from django.conf import settings
from ..models import MenuLink

register = template.Library()


@register.simple_tag
def get_pages_menu_links():
    """
    Simple tag

    :return: menu links that have attached pages
    """
    return MenuLink.objects.have_pages()


@register.inclusion_tag('common_content/json-ld.html', takes_context=True)
def page_json_ld(context):
    """
    Renders JSON-LD for a page

    :param context: parent template context
    :type context: dict
    :return: context for json-ld template
    :rtype: dict
    """
    site_url = '{}://{}'.format(
        context['request'].scheme,
        context['request'].get_host()
    )
    try:
        featured_image_url = site_url + context['menu_link'].page.featured_image.url
    except AttributeError:
        featured_image_url = site_url + settings.DEFAULT_FEATURED_IMAGE
    json_ld = {
        '@context': 'http://schema.org',
        '@type': 'WebPage',
        'name': context['menu_link'].page.title,
        'url': site_url + context['request'].path,
        'description': context['menu_link'].page.meta_description,
        'image': {
            '@type': 'imageObject',
            'url': featured_image_url
        },
    }
    return {'json_ld': json.dumps(json_ld, indent=2)}

# coding: utf-8
# Created on: 10.10.2016
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

import json
from django import template
from ..utils import get_site_config

register = template.Library()
register.simple_tag(get_site_config)


@register.inclusion_tag('common_content/json-ld.html', takes_context=True)
def site_json_ld(context):
    """
    Renders JSON-LD for the site

    :param context: parent template context
    :type context: dict
    :return: context for json-ld template
    :rtype: dict
    """
    site_url = '{}://{}'.format(
        context['request'].scheme,
        context['request'].get_host()
    )
    social = [
        context['site_config'].facebook,
        context['site_config'].twitter,
        context['site_config'].linkedin,
        context['site_config'].github,
        context['site_config'].stackoverflow
    ]
    json_ld = {
        '@context': 'http://schema.org',
        '@type': 'WebSite',
        'name': context['site_config'].site_name,
        'url': site_url,
        'sameAs': [item for item in social if item],
        'potentialAction': {
            '@type': 'SearchAction',
            'target': site_url + '/search/?q={search_term}',
            'query-input': 'required name=search_term'
            }
        }
    return {'json_ld': json.dumps(json_ld, indent=2)}

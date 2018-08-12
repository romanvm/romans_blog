# coding: utf-8
# Module: blog_tags
# Created on: 25.11.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

import json
from collections import namedtuple
from urllib.parse import quote_plus
from django import template
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.core.paginator import EmptyPage
from ..models import Category, Post

register = template.Library()
SideBarObjects = namedtuple('SideBarObjects', ['objects', 'more'])
MenuLink = namedtuple('MenuLink', ['caption', 'url'])


@register.simple_tag
def get_categories():
    """
    Simple tag

    :return: list of non-empty categories ordered by post count in desc. order
    """
    return Category.objects.ordered_by_post_count()


@register.simple_tag
def get_posts_digest(featured=False, posts_count=3):
    """
    Simple tag

    Get the lists of the latest posts (general of featured) for the blog sidebar

    :param featured: if ``True`` featured posts digest is returned
    :param posts_count: the number of posts to include in a digest
    :return: the digest of recent posts and "More" link
    :rtype: :class:`SideBarObjects`
    """
    if featured:
        posts = Post.objects.featured()
        more_link = reverse('blog:featured_posts')
    else:
        posts = Post.objects.published()
        more_link = reverse('blog:home')
    more = more_link if posts.count() > posts_count else None
    return SideBarObjects(posts[:posts_count], more)


@register.simple_tag
def get_archive_digest(months_count=6):
    """
    Simple tag

    :param months_count: the number of month to include in a digest
    :return: the list of the most recent months from the blog archive for the blog sidebar
    :rtype: :class:`SideBarObjects`
    """
    months = Post.objects.published().dates('date_published', 'month', order='DESC')
    more = reverse('blog:archive') if months.count() > months_count else None
    return SideBarObjects(months[:months_count], more)


@register.simple_tag
def get_blog_menu_links():
    """
    Simple tag

    :return: blog menu links for the site main menu.
    """
    featured = Post.objects.featured()
    featured_link = reverse('blog:featured_posts') if featured.exists() else None
    return (
        MenuLink(_('Recent Posts'), reverse('blog:home')),
        MenuLink(_('Featured Posts'), featured_link),
        MenuLink(_('Categories'), reverse('blog:categories_list')),
        MenuLink(_('Archive'), reverse('blog:archive'))
    )


@register.inclusion_tag('{0}/paginator.html'.format(settings.CURRENT_SKIN), takes_context=True)
def render_paginator(context, adjacent_pages=2):
    """
    Inclusion tag

    Renders paginator for multi-page lists.

    A skin must provide the respective paginator template.

    Adds pagination context variables for use in displaying first, adjacent and
    last page links in addition to those created by the object_list generic
    view.

    :param context: parent template context
    :param adjacent_pages: the number of pages adjacent to the current
    :return: rendered paginator html code
    """
    start_page = max(context['page_obj'].number - adjacent_pages, 1)
    if start_page <= 3:
        start_page = 1
    end_page = context['page_obj'].number + adjacent_pages + 1
    if end_page >= context['paginator'].num_pages - 1:
        end_page = context['paginator'].num_pages + 1
    page_numbers = [n for n in range(start_page, end_page) if n in range(1, context['paginator'].num_pages + 1)]
    page_obj = context['page_obj']
    paginator = context['paginator']
    try:
        next_ = context['page_obj'].next_page_number()
    except EmptyPage:
        next_ = None
    try:
        previous = context['page_obj'].previous_page_number()
    except EmptyPage:
        previous = None
    return {
        'page_obj': page_obj,
        'paginator': paginator,
        'page': context['page_obj'].number,
        'pages': context['paginator'].num_pages,
        'page_numbers': page_numbers,
        'next': next_,
        'previous': previous,
        'has_next': context['page_obj'].has_next(),
        'has_previous': context['page_obj'].has_previous(),
        'show_first': 1 not in page_numbers,
        'show_last': context['paginator'].num_pages not in page_numbers,
        'request': context['request'],
        'query': quote_plus(context['query']),
    }


@register.simple_tag(takes_context=True)
def check_blog_url(context):
    """
    Check if a current URL belong to blog application

    :param context: template context
    :type context: dict
    :return: check result
    :rtype: bool
    """
    return context['request'].path in [item.url for item in get_blog_menu_links()]


@register.inclusion_tag('common_content/json-ld.html', takes_context=True)
def blog_json_ld(context):
    """
    Renders JSON-LD for the blog

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
        site_logo_url = site_url + context['site_config'].site_logo.url
    except AttributeError:
        site_logo_url = site_url + settings.DEFAULT_LOGO
    json_ld = {
        '@context': 'http://schema.org',
        '@type': 'Blog',
        'name': context['site_config'].site_name,
        'url': site_url,
        'description': context['site_config'].site_tagline,
        'publisher': {
            '@type': 'Organization',
            'name': context['site_config'].site_name,
            'logo': {
                '@type': 'imageObject',
                'url': site_logo_url
            }
        }
    }
    return {'json_ld': json.dumps(json_ld, indent=2)}


@register.inclusion_tag('common_content/json-ld.html', takes_context=True)
def blog_post_json_ld(context):
    """
    Renders JSON-LD for the blog

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
        featured_image_url = site_url + context['post'].featured_image.url
    except AttributeError:
        featured_image_url = site_url + settings.DEFAULT_FEATURED_IMAGE
    try:
        site_logo_url = site_url + context['site_config'].site_logo.url
    except AttributeError:
        site_logo_url = site_url + settings.DEFAULT_LOGO
    json_ld = {
        '@context': 'https://schema.org',
        '@type': 'BlogPosting',
        'headline': context['post'].title,
        'description': context['post'].meta_description,
        'datePublished': context['post'].date_published.strftime('%Y-%m-%d'),
        'dateModified': context['post'].last_updated.strftime('%Y-%m-%d'),
        'image': {
            '@type': 'imageObject',
            'url': featured_image_url,
        },
        'publisher': {
            '@type': 'Organization',
            'name': context['site_config'].site_name,
            'logo': {
                '@type': 'imageObject',
                'url': site_logo_url
            }
        },
        'author': {
            '@type': 'Person',
            'name': 'Roman Miroshnychenko'  # todo: implement Post.author field
        },
        'keywords': ', '.join([category.name for category in context['post'].categories.all()]),
        'mainEntityOfPage': site_url + context['request'].path,
        'articleBody': context['post'].content
        }
    return {'json_ld': json.dumps(json_ld, indent=2)}

# coding: utf-8
# Module: blog_tags
# Created on: 25.11.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from collections import namedtuple
from urllib.parse import quote_plus
from django import template
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext
from django.core.paginator import EmptyPage
from django.db.models import Count
from ..models import Category, Post

_ = ugettext
register = template.Library()
SideBarObjects = namedtuple('SideBarObjects', ['objects', 'more'])


@register.simple_tag
def get_site_name():
    """
    Simple tag

    :return: site name from settings
    """
    return settings.SITE_NAME


@register.assignment_tag
def get_disqus_shortname():
    """
    Assignment tag

    :return: Disqus short name
    """
    return settings.DISQUS_SHORTNAME


@register.inclusion_tag('blog/disqus_comments.html', takes_context=True)
def render_disqus_comments(context):
    """
    Inclusion tag

    Render Disqus comments code

    If ``settings.DISQUS_SHORTNAME`` is empty, comments won't be rendered

    :param context: parent template context
    :return: rendered Disqus html/JS code.
    """
    return {'request': context['request'],
            'post': context['post'],
            'disqus_shortname': settings.DISQUS_SHORTNAME}


@register.assignment_tag
def get_categories():
    """
    Assignment tag

    :return: list of non-empty categories ordered by post count in desc. order
    """
    queryset = Category.objects.filter(posts__isnull=False).annotate(
            posts_count=Count('posts')).order_by('-posts_count', 'name')
    return [category for category in queryset if category.get_published_posts_count()]


@register.assignment_tag
def get_posts_digest(featured=False):
    """
    Assignment tag

    Get the lists of the latest posts (general of featured) for the blog sidebar

    :param featured: if ``True`` featured posts digest is returned
    :return: the digest of recent posts and "More" link
    :rtype: :class:`SideBarObjects`
    """
    posts = Post.objects.filter(is_published=True)
    if featured:
        posts = posts.filter(is_featured=True)
        more_link = reverse('blog:featured_posts')
    else:
        more_link = reverse('blog:home')
    more = more_link if posts.count() > settings.BLOG_SIDEBAR_POSTS_COUNT else None
    return SideBarObjects(posts[:settings.BLOG_SIDEBAR_POSTS_COUNT], more)


@register.assignment_tag
def get_archive_digest():
    """
    Assignment tag

    :return: the list of the most recent months from the blog archive for the blog sidebar
    :rtype: :class:`SideBarObjects`
    """
    months = Post.objects.filter(is_published=True).dates('date_published', 'month', order='DESC')
    more = reverse('blog:archive') if months.count() > settings.BLOG_SIDEBAR_POSTS_COUNT else None
    return SideBarObjects(months[:settings.BLOG_SIDEBAR_MONTHS_COUNT], more)


@register.assignment_tag
def get_blog_menu_links():
    """
    Assignment tag

    :return: blog menu links for the site main menu.
    """
    MenuLink = namedtuple('MenuLink', ['caption', 'url'])
    featured = Post.objects.filter(is_featured=True)
    featured_link = reverse('blog:featured_posts') if featured.count() else None
    return (
        MenuLink(_('Home'), reverse('blog:home')),
        MenuLink(_('Featured'), featured_link),
        MenuLink(_('Archive'), reverse('blog:archive'))
    )


@register.assignment_tag
def get_url(url_name, *args, **kwargs):
    """
    Assignment tag

    Get reverse URL as a template variable

    :param url_name: the name of a path from urls
    :return: relative URL path
    """
    return reverse(url_name, args=args, kwargs=kwargs)


@register.inclusion_tag('{0}/paginator.html'.format(settings.CURRENT_SKIN), takes_context=True)
def paginator(context, adjacent_pages=2):
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
    if start_page <= 3: start_page = 1
    end_page = context['page_obj'].number + adjacent_pages + 1
    if end_page >= context['paginator'].num_pages - 1:
        end_page = context['paginator'].num_pages + 1
    page_numbers = [n for n in range(start_page, end_page) if n > 0 and n <= context['paginator'].num_pages]
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


@register.inclusion_tag('blog/google_analytics.html', takes_context=False)
def render_google_analytics():
    """
    Inclusion tag

    Renders Google Analytics JS code

    If ``settings.GOOGLE_ANALYTICS_ID`` is empty, no code will be rendered.

    :return: rendered GA html code.
    """
    return {'google_analytics_id': settings.GOOGLE_ANALYTICS_ID}

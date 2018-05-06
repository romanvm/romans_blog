from django import template
from blog.utils import post_truncator

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
        categories.append('<a href="{url}">{name}</a>'.format(
            url=category.get_absolute_url(), name=category.name)
        )
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
    return post_truncator(
        post,
        '<span class="text-secondary">(<a href="{0}">{1}</a>)</span>'.format(
            post.get_absolute_url(), '...'
        )
    )

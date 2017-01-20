# coding: utf-8
# Created on: 09.03.2016
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

import re
from bs4 import BeautifulSoup
from django.conf import settings


def post_truncator(post, terminator):
    """
    Truncate a Post text to a page separator.

    The separator is inserted by TinyMCE ``pagebreak`` plugin
    that is used to emulate "blog post cut" feature.

    Only the 1st separator is taken into account, other separators, if any,
    are ignored.

    :param post: blog post
    :param terminator: terminating string or html code (e.g. "Read more..")
        that is appended to the end of the truncated post.
    :return: properly terminated truncated post
    """
    post_parts = post.content.split(settings.TINYMCE_DEFAULT_CONFIG['pagebreak_separator'])
    if len(post_parts) > 1:
        truncated_html = post_parts[0]
        post_digest = str(BeautifulSoup(truncated_html, 'html.parser'))
        end_tag = re.search(r'</\w+?>$', post_digest, re.UNICODE | re.IGNORECASE).group(0)
        if end_tag.lower() == '</p>':
            return post_digest[:-4] + ' ' + terminator + '</p>'
        else:
            return post_digest + '<p>' + terminator + '</p>'
    else:
        return post.content

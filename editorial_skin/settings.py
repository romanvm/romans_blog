# coding: utf-8
# Created on: 06.10.2017
# Author: Roman Miroshnychenko aka Roman V.M. (roman1972@gmail.com)

from django.contrib.staticfiles.storage import staticfiles_storage

BLOG_POSTS_PAGINATE_BY = 5

# Content styles for TinyMCE 4
CONTENT_CSS = [
    staticfiles_storage.url('editorial_skin/css/main.css'),
    staticfiles_storage.url('editorial_skin/css/editorial-skin.css'),
]

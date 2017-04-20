# coding: utf-8
# Module: page_tags
# Created on: 19.11.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from django import template
from ..models import MenuLink

register = template.Library()


@register.simple_tag
def get_pages_menu_links():
    """
    Simple tag

    :return: menu links that have attached pages
    """
    return MenuLink.objects.have_pages()

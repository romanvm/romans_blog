# coding: utf-8
# Module: templatetags_tests
# Created on: 19.11.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from django.test import TestCase
from .models import Page, MenuLink
from .templatetags.pages_tags import get_pages_menu_links


class GetMenuLinksTestCase(TestCase):
    """
    Test page view
    """
    def test_opening_page(self):
        page = Page(title='Page', content='')
        page.save()
        MenuLink.objects.create(caption='Page 1', slug='page-1', page=page)
        MenuLink.objects.create(caption='Page 2', slug='page-2')
        menu_links = get_pages_menu_links()
        self.assertEqual(len(menu_links), 1)
        self.assertEqual(menu_links[0].caption, 'Page 1')

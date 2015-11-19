# coding: utf-8
# Module: templatetags_tests
# Created on: 19.11.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from django.test import TestCase
from ..models import Page, MenuLink


class GetMenuLinksTestCase(TestCase):
    """
    Test page view
    """
    def test_opening_page(self):
        page = Page(title='Page', content='')
        page.save()
        menu_link1 = MenuLink(caption='Page 1', path='/page-1/', page=page)
        menu_link1.save()
        menu_link2 = MenuLink(caption='Page 2', path='/page-2/', page=page)
        menu_link2.save()
        response = self.client.get('/page-1/')
        self.assertIn('menu_links', response.context)
        self.assertEqual(len(response.context['menu_links']), 2)

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
        self.fail('Not implemented!')
        page = Page(title='Page', content='')
        page.save()
        MenuLink.objects.create(caption='Page 1', slug='page-1', page=page)
        MenuLink.objects.create(caption='Page 2', slig='page-2', page=page)
        response = self.client.get('/page-1/')
        self.assertIn('menu_links', response.context)
        self.assertContains(response, 'Page 1')
        self.assertContains(response, 'Page 2')

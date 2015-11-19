# coding: utf-8
# Module: views_tests
# Created on: 19.11.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from django.test import TestCase
from ..models import Page, MenuLink
from .models_tests import page_content


class PageViewTestCase(TestCase):
    """
    Test page view
    """
    def test_opening_page(self):
        page = Page(title='Page', keywords='lorem, ipsum', content=page_content)
        page.save()
        menu_link = MenuLink(caption='Page', path='/page/', page=page)
        menu_link.save()
        response = self.client.get('/page/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['path'], '/page/')
        self.assertEqual(response.context['title'], 'Page')
        self.assertEqual(response.context['keywords'], 'lorem, ipsum')
        self.assertEqual(response.context['content'], page_content)


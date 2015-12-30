# coding: utf-8
# Module: views_tests
# Created on: 19.11.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from django.core.urlresolvers import reverse
from django.test import TestCase
from .models import Page, MenuLink


class PageViewTestCase(TestCase):
    def test_opening_page_view(self):
        page = Page(title='Lorem Ipsum', content='<b>Lorem ipsum dolor sit amet.</b>')
        page.save()
        link1 = MenuLink(caption='Page 1', slug='page-1', page=page)
        link1.save()
        link2 = MenuLink(caption='Page 2', slug='page-2')
        link2.save()
        response = self.client.get(reverse('pages:page', kwargs={'slug': 'page-1'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Lorem ipsum dolor sit amet.')
        response = self.client.get(reverse('pages:page', kwargs={'slug': 'page-2'}))
        self.assertEqual(response.status_code, 404)

# coding: utf-8
# Module: models_tests
# Created on: 18.11.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from django.test import TestCase
from ..models import Page

page_content = """
<h1>Lorem ipsum</h1>
<p>Lorem ipsum dolor sit amet</p>
"""

class PageModelTestCase(TestCase):
    """
    Test for page model
    """
    def test_creating_page_objects(self):
        Page.objects.create(title='Page 2', content=page_content)
        Page.objects.create(title='Page 1', content=page_content)
        titles = [page.title for page in Page.objects.all()]
        self.assertEqual(titles, ['Page 1', 'Page 2'])

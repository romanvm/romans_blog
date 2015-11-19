# coding: utf-8
# Module: models_tests
# Created on: 18.11.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import Page, MenuLink

page_content = """
<h1>Lorem ipsum</h1>
<p>Lorem ipsum dolor sit amet</p>
"""

class PageModelTestCase(TestCase):
    """
    Test for Page model
    """
    def test_creating_page_objects(self):
        Page.objects.create(title='Page 2', content=page_content)
        Page.objects.create(title='Page 1', content=page_content)
        titles = [page.title for page in Page.objects.all()]
        self.assertEqual(titles, ['Page 1', 'Page 2'])


class MenuLinkTestCase(TestCase):
    """
    Test for MenuLink model
    """
    def test_creating_menu_link_objects(self):
        MenuLink.objects.create(caption='Page 2', path='/page-2/')
        MenuLink.objects.create(caption='Page 1', path='/page-1')
        captions = [link.caption for link in MenuLink.objects.all()]
        self.assertEqual(captions, ['Page 2', 'Page 1'])

    def test_validating_link_path_format(self):
        link1 = MenuLink(caption='Page 1', path='/page-1/')
        try:
            link1.clean()
        except ValidationError:
            self.fail('Correct path validation failed!')
        link2 = MenuLink(caption='Page 2', path='/page-1*?')
        self.assertRaises(ValidationError, link2.clean)

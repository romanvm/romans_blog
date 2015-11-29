# coding: utf-8
# Module: templatetags_tests
# Created on: 25.11.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.conf import settings


class TemplateTagsTestCase(TestCase):
    def test_get_site_name(self):
        response = self.client.get(reverse('blog:blog_home'))
        self.assertIn(settings.SITE_NAME, response.rendered_content)

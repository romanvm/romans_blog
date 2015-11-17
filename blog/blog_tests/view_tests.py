# coding: utf-8
# Module: view_tests
# Created on: 17.11.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from django.test import TestCase


class IndexViewTestCase(TestCase):
    """Test Index View"""
    def test_opening_index_view(self):
        """
        Test if index view opens correctly
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

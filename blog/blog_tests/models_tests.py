# coding: utf-8
# Module: models_tests
# Created on: 20.11.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from django.db.utils import IntegrityError
from django.test import TestCase
from ..models import Category


class CategoryTestCase(TestCase):
    """
    Test case for Category model
    """
    def setUp(self):
        Category.objects.create(name='Category 2', slug='category-2')
        Category.objects.create(name='Category 1', slug='category-1')

    def test_category_objects_creation(self):
        categories = [category.name for category in Category.objects.all()]
        self.assertEqual(categories, ['Category 1', 'Category 2'])

    def test_creation_with_duplicate_names(self):
        self.assertRaises(IntegrityError, Category.objects.create, name='Category 1', slug='category-11')

    def test_creation_with_duplicate_slugs(self):
        self.assertRaises(IntegrityError, Category.objects.create, name='Category 11', slug='category-2')

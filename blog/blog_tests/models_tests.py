# coding: utf-8
# Module: models_tests
# Created on: 20.11.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from datetime import datetime
from django.db.utils import IntegrityError
from django.test import TestCase
from ..models import Category, Post


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

    def test_populating_slug_field(self):
        category1 = Category(name='Lorem Ipsum')
        category1.clean()
        self.assertEqual(category1.slug, 'lorem-ipsum')
        category2 = Category(name='Тест')
        category2.clean()
        self.assertEqual(category2.slug, 'test')


class PostTestCase(TestCase):
    """
    Test case for Post model
    """
    def setUp(self):
        Post.objects.create(title='Post 1', date_published=datetime(year=2015, month=1, day=2),
                            slug='post-1', content='<p>Lorem ipsum<p>')
        Post.objects.create(title='Post 2', date_published=datetime(year=2015, month=1, day=1),
                            slug='post-2', content='<p>Lorem ipsum<p>')
        Post.objects.create(title='Post 3', date_published=datetime(year=2015, month=1, day=1),
                            slug='post-3', content='<p>Lorem ipsum<p>')
        titles = [post.title for post in Post.objects.all()]
        self.assertEqual(titles, ['Post 1', 'Post 3', 'Post 2'])

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

    def test_autopopulating_slug_field(self):
        category = Category(name='Lorem Ipsum')
        category.clean()
        self.assertEqual(category.slug, 'lorem-ipsum')
        category = Category(name='Тест')
        category.clean()
        self.assertEqual(category.slug, 'test')
        category = Category(name='Test', slug='lorem-ipsum')
        category.clean()
        self.assertEqual(category.slug, 'lorem-ipsum')


class PostTestCase(TestCase):
    """
    Test case for Post model
    """
    def test_creating_post_objects(self):
        Post.objects.create(title='Post 1', date_published=datetime(year=2015, month=1, day=2),
                            slug='post-1', content='<p>Lorem ipsum<p>')
        Post.objects.create(title='Post 2', date_published=datetime(year=2015, month=1, day=1),
                            slug='post-2', content='<p>Lorem ipsum<p>')
        Post.objects.create(title='Post 3', date_published=datetime(year=2015, month=1, day=1),
                            slug='post-3', content='<p>Lorem ipsum<p>')
        titles = [post.title for post in Post.objects.all()]
        self.assertEqual(titles, ['Post 1', 'Post 3', 'Post 2'])

    def test_autopopulating_slug_field(self):
        post = Post(title='Lorem Ipsum', content='<p>Lorem ipsum<p>')
        post.clean()
        self.assertEqual(post.slug, 'lorem-ipsum')
        post = Post(title='Тест', content='<p>Lorem ipsum<p>')
        post.clean()
        self.assertEqual(post.slug, 'test')
        post = Post(title='Test', slug='lorem-ipsum', content='<p>Lorem ipsum<p>')
        self.assertEqual(post.slug, 'lorem-ipsum')

    def test_autopopulating_date_fields(self):
        post = Post(title='Lorem Ipsum', slug='lorem-ipsum', content='<p>Lorem ipsum<p>')
        post.clean()
        self.assertFalse(post.date_published)
        self.assertFalse(post.date_updated)
        post.is_published = True
        post.clean()
        self.assertTrue(post.date_published)
        self.assertFalse(post.date_updated)
        post.clean()
        self.assertTrue(post.date_published)
        self.assertTrue(post.date_updated)

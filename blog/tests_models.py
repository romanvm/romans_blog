# coding: utf-8
# Module: models_tests
# Created on: 20.11.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from datetime import date
from django.db.utils import IntegrityError
from django.test import TestCase
from .models import Category, Post


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


class PostTestCase(TestCase):
    """
    Test case for Post model
    """
    def test_creating_post_objects(self):
        Post.objects.create(title='Post 1', date_published=date(year=2015, month=1, day=2),
                            slug='post-1', content='<p>Lorem ipsum<p>')
        Post.objects.create(title='Post 2', date_published=date(year=2015, month=1, day=1),
                            slug='post-2', content='<p>Lorem ipsum<p>')
        Post.objects.create(title='Post 3', date_published=date(year=2015, month=1, day=1),
                            slug='post-3', content='<p>Lorem ipsum<p>')
        titles = [post.title for post in Post.objects.all()]
        self.assertEqual(titles, ['Post 1', 'Post 3', 'Post 2'])

    def test_autopopulating_date_fields(self):
        post = Post(title='Lorem Ipsum', slug='lorem-ipsum', content='<p>Lorem ipsum<p>')
        post.save()
        self.assertFalse(post.date_published)
        post.is_published = True
        post.save()
        self.assertTrue(post.date_published)

    def test_get_absoluet_url(self):
        post = Post(title='Lorem Ipsum', slug='lorem-ipsum', content='<p>Lorem ipsum<p>', is_published=True)
        post.save()
        url = post.get_absolute_url()
        self.assertIn(str(post.pk), url)
        self.assertIn(post.slug, url)

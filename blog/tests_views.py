# coding: utf-8
# Module: view_tests
# Created on: 17.11.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from datetime import date
from django.test import TestCase
from .models import Category, Post


class BlogHomeViewTestCase(TestCase):
    """
    Test blog home view
    """
    def setUp(self):
        category1 = Category.objects.create(name='Category 1', slug='category-1')
        category2 = Category.objects.create(name='Category 2', slug='category-2')
        for d in range(1, 16):
            post = Post(title='Lorem Ipsum',
                        date_published=date(2015, 4, d),
                        slug='lorem-ipsum',
                        is_published=True,
                        content='<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>')
            post.save()
            post.categories.add(category1, category2)
            print('')

    def test_opening_blog_home(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Lorem Ipsum', response.rendered_content)
        self.assertIn('Category 1', response.rendered_content)

    def test_paginating_blog_home(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['page_obj'].paginator.num_pages, 3)
        self.assertFalse(response.context['page_obj'].has_previous())
        self.assertTrue(response.context['page_obj'].has_next())
        response = self.client.get('/blog/?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['page_obj'].has_previous())
        self.assertTrue(response.context['page_obj'].has_next())
        response = self.client.get('/blog/?page=3')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['page_obj'].has_previous())
        self.assertFalse(response.context['page_obj'].has_next())

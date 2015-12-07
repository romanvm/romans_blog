# coding: utf-8
# Module: view_tests
# Created on: 17.11.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from datetime import date
from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Category, Post


class BlogHomeViewTestCase(TestCase):
    def setUp(self):
        category1 = Category.objects.create(name='Category 1', slug='category-1')
        category1.save()
        category2 = Category.objects.create(name='Category 2', slug='category-2')
        category2.save()
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
        response = self.client.get(reverse('blog:blog_home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Lorem Ipsum', response.rendered_content)
        self.assertIn('Lorem ipsum dolor sit amet', response.rendered_content)
        self.assertIn('Category 1', response.rendered_content)
        self.assertIn('Category 2', response.rendered_content)

    def test_paginating_blog_home(self):
        response = self.client.get(reverse('blog:blog_home'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['page_obj'].paginator.num_pages, 3)
        self.assertFalse(response.context['page_obj'].has_previous())
        self.assertTrue(response.context['page_obj'].has_next())
        response = self.client.get(reverse('blog:blog_home'), {'page': '2'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['page_obj'].has_previous())
        self.assertTrue(response.context['page_obj'].has_next())
        response = self.client.get(reverse('blog:blog_home'), {'page': '3'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['page_obj'].has_previous())
        self.assertFalse(response.context['page_obj'].has_next())


class BlogFeaturedPostsViewTestCase(TestCase):
    def test_opening_featured_posts_view(self):
        for i in range(1, 6):
            Post.objects.create(title='Lorem Ipsum',
                                date_published=date(2015, 4, 28),
                                slug='lorem-ipsum',
                                is_published=True,
                                is_featured=(i % 2 != 0),
                                content='<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>')
        response = self.client.get(reverse('blog:featured_posts'))
        self.assertEqual(response.status_code, 200)
        self.assertEquals(len(response.context['posts']), 3)


class BlogPostViewTestCase(TestCase):
    def test_opening_blog_post(self):
        category = Category.objects.create(name='Category', slug='category')
        category.save()
        post = Post(title='Lorem Ipsum',
                    date_published=date(2015, 4, 28),
                    slug='lorem-ipsum',
                    is_published=False,
                    content='<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>')
        post.save()
        post.categories.add(category)
        response = self.client.get(reverse('blog:blog_post', kwargs={'slug': post.slug, 'pk': post.pk}))
        self.assertEquals(response.status_code, 404)
        post.is_published = True
        post.save()
        response = self.client.get(reverse('blog:blog_post', kwargs={'slug': post.slug, 'pk': post.pk}))
        self.assertEquals(response.status_code, 200)
        self.assertIn('Lorem Ipsum', response.rendered_content)
        self.assertIn('<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>', response.rendered_content)
        self.assertIn('Category', response.rendered_content)


class BlogCategoryViewTestCase(TestCase):
    def test_opening_posts_in_a_category(self):
        category = Category.objects.create(name='Category', slug='category')
        category.save()
        for i in range(7):
            post = Post(title='Lorem Ipsum {0}'.format(i),
                        date_published=date(2015, 4, 28),
                        slug='lorem-ipsum-{0}'.format(i),
                        is_published=True,
                        content='<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>')
            post.save()
            if i % 2 != 0:
                post.categories.add(category)
        response = self.client.get(reverse('blog:blog_category', kwargs={'slug': category.slug}))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.context['posts']), 3)
        response = self.client.get(reverse('blog:blog_category', kwargs={'slug': 'fail'}))
        self.assertEquals(response.status_code, 404)


class BlogCategoriesListViewTestCase(TestCase):
    def test_opening_categories_list(self):
        post = Post(title='Lorem Ipsum',
                    date_published=date(2015, 4, 28),
                    slug='lorem-ipsum',
                    is_published=True,
                    content='<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>')
        post.save()
        for i in range(7):
            category = Category.objects.create(name='Category {0}'.format(i), slug='category-{0}'.format(i))
            category.save()
            if i % 2 != 0:
                post.categories.add(category)
                post.save()
        response = self.client.get(reverse('blog:blog_categories_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['categories']), 3)

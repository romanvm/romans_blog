# coding: utf-8
# Module: templatetags_tests
# Created on: 25.11.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from datetime import date
from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Post, Category
from .templatetags.blog_tags import (get_posts_digest, get_archive_digest,
                                     get_categories, get_blog_menu_links)


class TemplateTagsTestCase(TestCase):
    def test_get_posts_digest(self):
        for i in range(1, 7):
            Post.objects.create(title='Post {}'.format(i),
                                date_published=date(year=2015, month=1, day=i),
                                slug='post-{}'.format(i),
                                content='<p>Lorem ipsum<p>')
        latest_posts = get_posts_digest(False, 5)
        self.assertEqual(len(latest_posts.objects), 0)
        posts = Post.objects.all()
        for post in posts[:5]:
            post.is_published = True
            post.save()
        latest_posts = get_posts_digest(False, 5)
        self.assertEqual(len(latest_posts.objects), 5)
        self.assertIs(latest_posts.more, None)
        for post in posts[5:]:
            post.is_published = True
            post.save()
        latest_posts = get_posts_digest(False, 5)
        self.assertEqual(len(latest_posts.objects), 5)
        self.assertEqual(latest_posts.more, reverse('blog:home'))
        for post in posts:
            post.is_featured = True
            post.save()
        featured_posts = get_posts_digest(True, 5)
        self.assertEqual(len(featured_posts.objects), 5)
        self.assertEqual(featured_posts.more, reverse('blog:featured_posts'))

    def test_get_archive_digest(self):
        for m in range(1, 6):
            Post.objects.create(title='Post {}'.format(m),
                                date_published=date(year=2015, month=m, day=1),
                                slug='post-{}'.format(m),
                                content='<p>Lorem ipsum<p>')
        months = get_archive_digest(5)
        self.assertEqual(len(months.objects), 0)
        self.assertIs(months.more, None)
        for post in Post.objects.all():
            post.is_published = True
            post.save()
        months = get_archive_digest(5)
        self.assertEqual(len(months.objects), 5)
        self.assertIs(months.more, None)
        for m in range(6, 13):
            Post.objects.create(title='Post {}'.format(m),
                            date_published=date(year=2015, month=m, day=1),
                            slug='post-{}'.format(m),
                            content='<p>Lorem ipsum<p>',
                            is_published=True)
        months = get_archive_digest(7)
        self.assertEqual(len(months.objects), 7)
        self.assertEqual(months.more, reverse('blog:archive'))

    def test_get_categories(self):
        cat_list = []
        for i in range(7):
            category = Category.objects.create(name='Category {0}'.format(i), slug='category-{0}'.format(i))
            category.save()
            cat_list.append(category)
        for i in range(7):
            post = Post(title='Lorem Ipsum {0}'.format(i),
                        date_published=date(2015, 4, 28),
                        slug='lorem-ipsum-{0}'.format(i),
                        is_published=True,
                        content='<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>')
            post.save()
            for cat in cat_list[i:]:
                post.categories.add(cat)
        categories = list(get_categories())
        self.assertEqual(len(categories), 7)
        self.assertEqual(categories[0], cat_list[6])
        self.assertEqual(categories[6], cat_list[0])

    def test_get_blog_menu_links(self):
        self.assertEqual(len(get_blog_menu_links()), 4)

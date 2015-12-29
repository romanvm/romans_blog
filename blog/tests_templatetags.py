# coding: utf-8
# Module: templatetags_tests
# Created on: 25.11.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from datetime import date
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.conf import settings
from .models import Post
from .templatetags.blog_tags import get_posts_digest, get_archive_digest


class TemplateTagsTestCase(TestCase):
    def test_get_site_name(self):
        response = self.client.get(reverse('blog:home'))
        self.assertIn(settings.SITE_NAME, response.rendered_content)

    def test_get_posts_digest(self):
        for i in range(1, 7):
            Post.objects.create(title='Post {}'.format(i),
                                date_published=date(year=2015, month=1, day=i),
                                slug='post-{}'.format(i),
                                content='<p>Lorem ipsum<p>')
        with self.settings(BLOG_SIDEBAR_POSTS_COUNT=3):
            latest_posts = get_posts_digest(False)
            self.assertEqual(len(latest_posts.objects), 0)
            posts = Post.objects.all()
            for post in posts[:3]:
                post.is_published = True
                post.save()
            latest_posts = get_posts_digest(False)
            self.assertEqual(len(latest_posts.objects), 3)
            self.assertIs(latest_posts.more, None)
            for post in posts[3:]:
                post.is_published = True
                post.save()
            latest_posts = get_posts_digest(False)
            self.assertEqual(len(latest_posts.objects), 3)
            self.assertEqual(latest_posts.more, reverse('blog:home'))
            for post in posts:
                post.is_featured = True
                post.save()
            featured_posts = get_posts_digest(True)
            self.assertEqual(len(featured_posts.objects), 3)
            self.assertEqual(featured_posts.more, reverse('blog:featured_posts'))

    def test_get_archive_digest(self):
        for m in range(1, 4):
            Post.objects.create(title='Post {}'.format(m),
                                date_published=date(year=2015, month=m, day=1),
                                slug='post-{}'.format(m),
                                content='<p>Lorem ipsum<p>')
        with self.settings(BLOG_SIDEBAR_MONTHS_COUNT=6):
            months = get_archive_digest()
            self.assertEqual(len(months.objects), 0)
            self.assertIs(months.more, None)
            for post in Post.objects.all():
                post.is_published = True
                post.save()
            months = get_archive_digest()
            self.assertEqual(len(months.objects), 3)
            self.assertIs(months.more, None)
            for m in range(4, 13):
                Post.objects.create(title='Post {}'.format(m),
                                date_published=date(year=2015, month=m, day=1),
                                slug='post-{}'.format(m),
                                content='<p>Lorem ipsum<p>',
                                is_published=True)
            months = get_archive_digest()
            self.assertEqual(len(months.objects), 6)
            self.assertEqual(months.more, reverse('blog:archive'))

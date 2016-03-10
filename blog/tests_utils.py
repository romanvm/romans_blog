# coding: utf-8
# Module: tests_utils
# Created on: 10.03.2016
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from collections import namedtuple
from unittest import TestCase
from .utils import post_truncator

FakePost = namedtuple('FakePost', ['content'])


class PostTruncatorTestCase(TestCase):
    def test_non_truncated_post(self):
        content = '<p>Lorem ipsum dolor sit amet.</p>'
        post = FakePost(content)
        result = post_truncator(post, '...')
        self.assertFalse('...' in result)

    def test_truncated_paragraph(self):
        content = '<p>Lorem ipsum dolor<!-- ***Blog Cut*** --> sit amet.</p>'
        post = FakePost(content)
        result = post_truncator(post, '...')
        self.assertTrue('...' in result)
        self.assertEqual(result[-4:], '</p>')

    def test_truncated_pre_block(self):
        content = '<p>Lorem ipsum</p><pre>dolor<!-- ***Blog Cut*** --> sit amet.</pre>'
        post = FakePost(content)
        result = post_truncator(post, '...')
        self.assertTrue('...' in result)
        self.assertEqual(result[-4:], '</p>')
        self.assertEqual(result[-10:-7], '<p>')

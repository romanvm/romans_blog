#!/usr/bin/env python3
# coding: utf-8
# Module: populate_db.py
# Created on: 24.11.2015
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

import os
from datetime import datetime
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'romans_blog.settings')
django.setup()

from pages.models import MenuLink, Page
from blog.models import Category, Post


with open('lorem_ipsum.html', mode='r') as file_obj:
    lorem_ipsum = file_obj.read()
# Create pages
print('Creating pages...')
page = Page.objects.create(title='Lorem Ipsum',
                           keywords='lorem, ipsum',
                           content=lorem_ipsum)
print('Creating menu links...')
for i in range(1, 4):
    MenuLink.objects.create(caption='Page {}'.format(i),
                            slug='page-{}'.format(i),
                            page=page)
# Create blog posts
print('Creating categories...')
category1 = Category.objects.create(name='Category 1', slug='category-1')
category2 = Category.objects.create(name='Category 2', slug='category-2')
print('Creating blog posts. It may take a while...')
for m in range(1, 13):
    for d in range(1, 29, 5):
        post = Post(title='Lorem Ipsum',
                    date_published=datetime(year=2014, month=m, day=d),
                    slug='lorem-ipsum',
                    is_published=True,
                    content=lorem_ipsum)
        post.save()
        post.categories.add(category1, category2)
print('Models created successfully.')

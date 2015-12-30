# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Category Name', unique=True, max_length=100)),
                ('slug', models.SlugField(verbose_name='Slug', unique=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='Title', db_index=True, max_length=200)),
                ('date_published', models.DateField(verbose_name='Date Published', blank=True, null=True)),
                ('last_updated', models.DateTimeField(verbose_name='Last Updated', auto_now=True)),
                ('slug', models.SlugField(verbose_name='Slug', max_length=200)),
                ('is_published', models.BooleanField(verbose_name='Published', default=False)),
                ('is_featured', models.BooleanField(verbose_name='Featured', default=False)),
                ('allow_comments', models.BooleanField(verbose_name='Allow comments', default=True)),
                ('content', tinymce.models.HTMLField(verbose_name='Post Content')),
                ('categories', models.ManyToManyField(verbose_name='Categories', blank=True, related_name='posts', to='blog.Category')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-date_published', '-pk'],
            },
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filebrowser.fields
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='Category Name')),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name='Slug')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='Title', db_index=True)),
                ('date_published', models.DateField(verbose_name='Date Published', blank=True)),
                ('slug', models.SlugField(max_length=200, verbose_name='Slug')),
                ('cover_image', filebrowser.fields.FileBrowseField(max_length=200, verbose_name='Cover Image', blank=True, null=True)),
                ('is_published', models.BooleanField(verbose_name='Published', default=False)),
                ('is_featured', models.BooleanField(verbose_name='Featured', default=False)),
                ('allow_comments', models.BooleanField(verbose_name='Allow comments', default=True)),
                ('content', tinymce.models.HTMLField(verbose_name='Post Content')),
                ('categories', models.ManyToManyField(related_name='posts', verbose_name='Categories', blank=True, to='blog.Category')),
            ],
            options={
                'ordering': ['-date_published', '-pk'],
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]

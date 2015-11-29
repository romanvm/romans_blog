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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='Category Name')),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name='Slug')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
                'verbose_name': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(db_index=True, max_length=200, verbose_name='Title')),
                ('date_published', models.DateField(blank=True, verbose_name='Date Published')),
                ('slug', models.SlugField(max_length=200, verbose_name='Slug')),
                ('cover_image', filebrowser.fields.FileBrowseField(blank=True, max_length=200, verbose_name='Cover Image')),
                ('is_published', models.BooleanField(verbose_name='Published', default=False)),
                ('is_featured', models.BooleanField(verbose_name='Featured', default=False)),
                ('allow_comments', models.BooleanField(verbose_name='Allow comments', default=True)),
                ('content', tinymce.models.HTMLField(verbose_name='Post Content')),
                ('categories', models.ManyToManyField(to='blog.Category', blank=True, related_name='posts', verbose_name='Categories', null=True)),
            ],
            options={
                'verbose_name_plural': 'Posts',
                'ordering': ['-date_published', '-pk'],
                'verbose_name': 'Post',
            },
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuLink',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('caption', models.CharField(max_length=200, verbose_name='Caption')),
                ('slug', models.SlugField(unique=True, max_length=200, verbose_name='Slug')),
            ],
            options={
                'ordering': ['pk'],
                'verbose_name': 'Menu Link',
                'verbose_name_plural': 'Menu Links',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='Page Title')),
                ('keywords', models.CharField(max_length=200, verbose_name='Keywords', blank=True)),
                ('content', tinymce.models.HTMLField(verbose_name='Page Content')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
            },
        ),
        migrations.AddField(
            model_name='menulink',
            name='page',
            field=models.ForeignKey(verbose_name='Page', to='pages.Page', blank=True),
        ),
    ]

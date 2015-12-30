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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('caption', models.CharField(verbose_name='Caption', max_length=200)),
                ('slug', models.SlugField(verbose_name='Slug', unique=True, max_length=200)),
                ('show_side_panel', models.BooleanField(verbose_name='Show side Panel', default=False)),
            ],
            options={
                'verbose_name': 'Menu Link',
                'verbose_name_plural': 'Menu Links',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='Page Title', max_length=200)),
                ('keywords', models.CharField(verbose_name='Keywords', blank=True, max_length=200)),
                ('content', tinymce.models.HTMLField(verbose_name='Page Content')),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='menulink',
            name='page',
            field=models.ForeignKey(to='pages.Page', verbose_name='Page', null=True, blank=True),
        ),
    ]

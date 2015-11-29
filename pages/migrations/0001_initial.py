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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('caption', models.CharField(max_length=200, verbose_name='Caption')),
                ('slug', models.SlugField(unique=True, max_length=200, verbose_name='Slug')),
            ],
            options={
                'verbose_name_plural': 'Menu Links',
                'ordering': ['pk'],
                'verbose_name': 'Menu Link',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='Page Title')),
                ('keywords', models.CharField(blank=True, max_length=200, verbose_name='Keywords')),
                ('content', tinymce.models.HTMLField(verbose_name='Page Content')),
            ],
            options={
                'verbose_name_plural': 'Pages',
                'ordering': ['title'],
                'verbose_name': 'Page',
            },
        ),
        migrations.AddField(
            model_name='menulink',
            name='page',
            field=models.ForeignKey(blank=True, to='pages.Page', null=True, verbose_name='Page'),
        ),
    ]

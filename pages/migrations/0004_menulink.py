# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_page_keywords'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=200, verbose_name='Caption')),
                ('path', models.CharField(max_length=200, verbose_name='Path')),
                ('page', models.ForeignKey(null=True, to='pages.Page', blank=True, verbose_name='Page')),
            ],
            options={
                'ordering': ['pk'],
                'verbose_name_plural': 'Menu Links',
                'verbose_name': 'Menu Link',
            },
        ),
    ]

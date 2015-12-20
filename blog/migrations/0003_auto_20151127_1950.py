# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20151127_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(to='blog.Category', verbose_name='Categories', related_name='posts', blank=True),
        ),
    ]

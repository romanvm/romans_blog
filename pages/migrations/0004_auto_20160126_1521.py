# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_page_meta_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='meta_description',
            field=models.TextField(max_length=160, verbose_name='Description', blank=True),
        ),
    ]

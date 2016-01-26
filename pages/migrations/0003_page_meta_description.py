# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_page_last_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_menulink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menulink',
            name='path',
            field=models.CharField(verbose_name='Path', unique=True, max_length=200),
        ),
    ]

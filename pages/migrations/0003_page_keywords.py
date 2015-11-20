# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20151118_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='keywords',
            field=models.CharField(verbose_name='Keywords', blank=True, max_length=200),
        ),
    ]

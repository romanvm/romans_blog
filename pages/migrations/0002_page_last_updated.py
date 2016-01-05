# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 5, 13, 24, 26, 267081, tzinfo=utc), auto_now=True, verbose_name='Last Updated'),
            preserve_default=False,
        ),
    ]

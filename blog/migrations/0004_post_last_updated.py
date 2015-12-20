# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20151127_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 30, 17, 35, 48, 797498, tzinfo=utc), verbose_name='Last Updated', auto_now=True),
            preserve_default=False,
        ),
    ]

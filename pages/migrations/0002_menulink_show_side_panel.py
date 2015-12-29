# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menulink',
            name='show_side_panel',
            field=models.BooleanField(verbose_name='Show side Panel', default=False),
        ),
    ]

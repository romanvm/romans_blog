# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='Page Title')),
                ('content', tinymce.models.HTMLField(verbose_name='Page Content')),
            ],
            options={
                'verbose_name_plural': 'Pages',
                'ordering': ['title'],
                'verbose_name': 'Pages',
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-10 10:54
from __future__ import unicode_literals

from django.db import migrations, models
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('common_content', '0002_siteconfiguration_robots_txt'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='facebook',
            field=models.CharField(blank=True, max_length=256, verbose_name='Facebook Profile'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='github',
            field=models.CharField(blank=True, max_length=256, verbose_name='GitHub Profile'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='linkedin',
            field=models.CharField(blank=True, max_length=256, verbose_name='LinkedIn Profile'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='site_logo',
            field=filebrowser.fields.FileBrowseField(blank=True, max_length=1024, verbose_name='Site Logo'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='stackoverflow',
            field=models.CharField(blank=True, max_length=256, verbose_name='Stackoverflow Profile'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='twitter',
            field=models.CharField(blank=True, max_length=256, verbose_name='Twitter Profile'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='maintenance_mode',
            field=models.BooleanField(default=False, verbose_name='Maintenance Mode'),
        ),
    ]
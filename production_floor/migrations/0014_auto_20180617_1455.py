# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-17 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production_floor', '0013_auto_20180617_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='CN',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='edition',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

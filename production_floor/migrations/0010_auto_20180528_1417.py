# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-28 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production_floor', '0009_auto_20180523_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='parameters',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
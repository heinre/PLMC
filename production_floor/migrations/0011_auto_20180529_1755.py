# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-29 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production_floor', '0010_auto_20180528_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='done_processes',
            field=models.TextField(blank=True, default='{}', null=True),
        ),
    ]

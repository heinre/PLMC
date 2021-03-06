# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-05 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20180402_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='contactEmail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='contactPhone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
    ]

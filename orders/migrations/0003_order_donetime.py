# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-03 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_duedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='doneTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

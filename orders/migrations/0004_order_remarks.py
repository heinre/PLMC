# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-05 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_donetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
    ]

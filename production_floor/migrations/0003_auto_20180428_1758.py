# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-28 14:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('production_floor', '0002_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='productName',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='orderId',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='machines',
            new_name='processes',
        ),
    ]

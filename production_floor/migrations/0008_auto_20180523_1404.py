# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-23 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production_floor', '0007_product_coc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='coc',
            field=models.FileField(blank=True, null=True, upload_to='media/coc/<django.db.models.fields.related.ForeignKey>'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-17 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production_floor', '0012_product_routing'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='coc_needed',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='density',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='diameter',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='freq',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='fs',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='hz',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='micro_weld',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='ms',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='others',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='power',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='rotating',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='schema',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='speed',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='volt',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

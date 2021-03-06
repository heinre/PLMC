# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-12 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_auto_20180405_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='PotentialClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=400)),
                ('contactName', models.CharField(max_length=100)),
                ('contactEmail', models.EmailField(blank=True, max_length=254, null=True)),
                ('contactPhone', models.CharField(blank=True, max_length=15, null=True)),
                ('field', models.CharField(max_length=400)),
                ('operator', models.CharField(max_length=100)),
                ('referred', models.CharField(choices=[('GL', 'Google'), ('WS', 'ביקור באתר'), ('NP', 'עיתון'), ('RC', 'המלצה'), ('OT', 'אחר')], default='OT', max_length=2)),
                ('remarks', models.TextField(blank=True, null=True)),
            ],
        ),
    ]

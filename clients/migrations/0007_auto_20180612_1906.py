# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-12 16:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_auto_20180612_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='potentialclient',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 12, 16, 6, 48, 129582, tzinfo=utc)),
        ),
    ]

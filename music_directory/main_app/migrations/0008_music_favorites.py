# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-13 23:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20170507_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='favorites',
            field=models.BooleanField(default=False),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-07 23:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20170506_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='lyrics',
            field=models.TextField(default='Your lyrics here: '),
        ),
        migrations.AlterField(
            model_name='music',
            name='video',
            field=models.URLField(null=True),
        ),
    ]
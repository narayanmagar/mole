# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 05:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0005_auto_20160504_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='group',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]

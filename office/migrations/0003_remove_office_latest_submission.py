# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 05:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0002_office_latest_submission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='office',
            name='latest_submission',
        ),
    ]

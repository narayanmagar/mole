# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 15:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sachibBaithak', '0003_auto_20170716_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sachibbaithak',
            name='sachibbaithakmain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sachibBaithak.SachibBaithakMain'),
        ),
    ]
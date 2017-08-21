# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 14:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0001_initial'),
        ('sachibBaithak', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SachibBaithakMain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateofbaithak', models.CharField(blank=True, max_length=10, null=True)),
                ('chairmanship', models.CharField(blank=True, max_length=10, null=True)),
                ('datesubmited', models.CharField(blank=True, max_length=10, null=True)),
                ('dateupdated', models.CharField(blank=True, max_length=10, null=True)),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office.Office')),
            ],
        ),
        migrations.AlterField(
            model_name='sachibbaithak',
            name='nirnayaharu',
            field=models.TextField(verbose_name='\u0928\u093f\u0930\u094d\u0923\u092f'),
        ),
        migrations.AddField(
            model_name='sachibbaithak',
            name='sachibbaithakmain',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sachibbaithakmains', to='sachibBaithak.SachibBaithakMain'),
            preserve_default=False,
        ),
    ]

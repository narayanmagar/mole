# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-14 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0022_auto_20180114_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lakxya',
            name='awadhi',
            field=models.IntegerField(choices=[(4, '\u092c\u093e\u0930\u094d\u0937\u093f\u0915'), (1, '\u092a\u094d\u0930\u0925\u092e'), (2, '\u0926\u093f\u0924\u093f\u092f'), (3, '\u0924\u0943\u0924\u0940\u092f')], default=0, verbose_name='\u0905\u0935\u0927\u093f'),
        ),
        migrations.AlterField(
            model_name='pragati',
            name='awadhi',
            field=models.IntegerField(choices=[(4, '\u092c\u093e\u0930\u094d\u0937\u093f\u0915'), (1, '\u092a\u094d\u0930\u0925\u092e'), (2, '\u0926\u093f\u0924\u093f\u092f'), (3, '\u0924\u0943\u0924\u0940\u092f')], default=1, verbose_name='\u0905\u0935\u0927\u093f'),
        ),
    ]

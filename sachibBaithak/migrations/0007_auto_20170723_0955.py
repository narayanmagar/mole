# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sachibBaithak', '0006_budgetbaktabya_office'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgetbaktabya',
            name='budhano',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='\u092c\u0941\u0926\u093e \u0928'),
        ),
        migrations.AlterField(
            model_name='budgetbaktabya',
            name='datesubmited',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='\u092a\u0947\u0936 \u0917\u0930\u093f\u090f\u0915\u094b \u0938\u092e\u092f '),
        ),
        migrations.AlterField(
            model_name='budgetbaktabya',
            name='dateupdated',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='\u0938\u091a\u094d\u092f\u093e\u0907\u090f\u0915\u094b \u0938\u092e\u092f '),
        ),
        migrations.AlterField(
            model_name='budgetbaktabya',
            name='karyakrams',
            field=models.TextField(blank=True, max_length=10, null=True, verbose_name='\u0915\u093e\u0930\u094d\u092f\u0915\u094d\u0930\u092e\u0939\u0930\u0941 '),
        ),
        migrations.AlterField(
            model_name='budgetbaktabya',
            name='pragati',
            field=models.TextField(blank=True, max_length=10, null=True, verbose_name='\u092a\u094d\u0930\u0917\u0924\u093f '),
        ),
        migrations.AlterField(
            model_name='budgetbaktabya',
            name='problems',
            field=models.TextField(blank=True, max_length=10, null=True, verbose_name='\u0938\u092e\u0938\u094d\u092f\u093e '),
        ),
        migrations.AlterField(
            model_name='budgetbaktabya',
            name='solutions',
            field=models.TextField(blank=True, max_length=10, null=True, verbose_name='\u0938\u093e\u0935\u0927\u093e\u0928 '),
        ),
        migrations.AlterField(
            model_name='sachibbaithak',
            name='datesubmited',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='\u092a\u0947\u0936 \u0917\u0930\u093f\u090f\u0915\u094b \u0938\u092e\u092f '),
        ),
        migrations.AlterField(
            model_name='sachibbaithak',
            name='dateupdated',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='\u0938\u091a\u094d\u092f\u093e\u0907\u090f\u0915\u094b \u0938\u092e\u092f '),
        ),
        migrations.AlterField(
            model_name='sachibbaithak',
            name='jimmewar_nikaya',
            field=models.CharField(max_length=100, verbose_name='\u091c\u093f\u092e\u094d\u092e\u0947\u0935\u093e\u0930 \u0928\u093f\u0915\u093e\u092f '),
        ),
        migrations.AlterField(
            model_name='sachibbaithak',
            name='karyanayan_awastha',
            field=models.TextField(verbose_name='\u0915\u0930\u094d\u092f\u0928\u092f\u0928 \u0905\u0935\u0938\u094d\u0925\u093e '),
        ),
        migrations.AlterField(
            model_name='sachibbaithak',
            name='nirnayaharu',
            field=models.TextField(verbose_name='\u0928\u093f\u0930\u094d\u0923\u092f\u0939\u0930\u0941 '),
        ),
        migrations.AlterField(
            model_name='sachibbaithakmain',
            name='chairmanship',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='\u0905\u0927\u094d\u092f\u0915\u094d\u0937\u0924\u093e '),
        ),
        migrations.AlterField(
            model_name='sachibbaithakmain',
            name='dateofbaithak',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='\u092c\u0948\u0920\u0915 \u0917\u0930\u093f\u090f\u0915\u094b \u092e\u093f\u0924\u093f '),
        ),
        migrations.AlterField(
            model_name='sachibbaithakmain',
            name='datesubmited',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='\u092a\u0947\u0936 \u0917\u0930\u093f\u090f\u0915\u094b \u0938\u092e\u092f '),
        ),
        migrations.AlterField(
            model_name='sachibbaithakmain',
            name='dateupdated',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='\u0938\u091a\u094d\u092f\u093e\u0907\u090f\u0915\u094b \u0938\u092e\u092f '),
        ),
    ]

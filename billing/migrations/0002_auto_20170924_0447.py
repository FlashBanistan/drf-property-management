# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-24 04:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charge',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

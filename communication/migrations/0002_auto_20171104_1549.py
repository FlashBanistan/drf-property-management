# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-04 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenancerequest',
            name='permission_to_enter',
            field=models.BooleanField(default=True),
        ),
    ]

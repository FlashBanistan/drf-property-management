# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-21 17:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='tenants',
        ),
    ]

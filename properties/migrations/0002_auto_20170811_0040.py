# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 00:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='property',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='building',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='property',
        ),
    ]

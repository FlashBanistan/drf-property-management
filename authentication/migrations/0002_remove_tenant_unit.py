# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-26 17:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenant',
            name='unit',
        ),
    ]
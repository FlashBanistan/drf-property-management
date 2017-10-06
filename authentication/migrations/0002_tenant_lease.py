# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-02 22:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('legal', '0001_initial'),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='lease',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='legal.Lease'),
        ),
    ]
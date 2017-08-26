# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-26 17:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_auto_20170826_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='property',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='properties.Property'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='baths',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='bedrooms',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='building',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='properties.Building'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='property',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='properties.Property'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='sq_ft',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-22 23:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import property_management.validators.phone_number


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('properties', '0003_auto_20170811_0103'),
    ]

    operations = [
        migrations.CreateModel(
            name='OccupantType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('occupant_type_id', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=11, null=True, validators=[property_management.validators.phone_number.validate_phone_number])),
                ('ssn', models.CharField(blank=True, max_length=11, null=True)),
                ('occupant_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tenants.OccupantType')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='properties.Unit')),
            ],
        ),
    ]

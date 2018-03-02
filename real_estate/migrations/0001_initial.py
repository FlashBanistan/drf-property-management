# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-02 19:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import property_management.validators.phone_number


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Complex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=11, validators=[property_management.validators.phone_number.validate_phone_number])),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=10)),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Complexes',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=10)),
                ('unit_number', models.CharField(default=None, max_length=10)),
                ('sq_ft', models.IntegerField(blank=True, null=True)),
                ('bedrooms', models.IntegerField(blank=True, null=True)),
                ('baths', models.FloatField(blank=True, null=True)),
                ('building', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='units', to='real_estate.Building')),
                ('complex', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='units', to='real_estate.Complex')),
            ],
        ),
        migrations.AddField(
            model_name='building',
            name='complex',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buildings', to='real_estate.Complex'),
        ),
    ]

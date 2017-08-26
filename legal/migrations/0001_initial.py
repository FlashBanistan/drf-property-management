# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-26 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
        ('properties', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(editable=False)),
                ('length', models.DurationField(help_text='Use the following format: D HH:MM:SS', unique=True)),
                ('leasees', models.ManyToManyField(to='authentication.Tenant')),
                ('leasors', models.ManyToManyField(to='properties.Property')),
            ],
        ),
    ]

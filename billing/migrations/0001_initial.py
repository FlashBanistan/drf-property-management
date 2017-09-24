# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-23 18:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
        ('legal', '0004_auto_20170923_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='Charge',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_due', models.DateField()),
                ('created_on', models.DateField(auto_now_add=True)),
                ('lease', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='legal.Lease')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('charge', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='billing.Charge')),
                ('paid_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.Tenant')),
            ],
        ),
    ]
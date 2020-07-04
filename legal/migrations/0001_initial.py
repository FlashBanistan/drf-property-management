# Generated by Django 3.0.3 on 2020-07-04 04:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('real_estate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lease',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('unit', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='real_estate.Unit')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

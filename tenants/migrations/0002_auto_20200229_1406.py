# Generated by Django 3.0.3 on 2020-02-29 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Client',
            new_name='Tenant',
        ),
    ]
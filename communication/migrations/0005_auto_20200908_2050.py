# Generated by Django 3.0.3 on 2020-09-09 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0004_maintenancerequest_date_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenancerequest',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('COMPLETED', 'Completed')], default='PENDING', max_length=12),
        ),
    ]
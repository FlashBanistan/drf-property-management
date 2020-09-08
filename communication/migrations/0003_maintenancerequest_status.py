# Generated by Django 3.0.3 on 2020-09-06 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0002_auto_20200703_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenancerequest',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('COMPLETED', 'Completed')], default='PENDING', max_length=12),
            preserve_default=False,
        ),
    ]

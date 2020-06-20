# Generated by Django 3.0.3 on 2020-06-18 02:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Charge',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('created', 'Created'), ('processed', 'Processed'), ('charged', 'Charged'), ('cancelled', 'Cancelled'), ('waived', 'Waived'), ('paid_in_full', 'Paid In Full'), ('paid_in_part', 'Paid In Part')], max_length=12)),
                ('date_processed', models.DateField(blank=True, null=True)),
                ('date_charged', models.DateField(blank=True, null=True)),
                ('date_due', models.DateField(blank=True, null=True)),
                ('paid_in_full_on', models.DateField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('payment_type', models.CharField(choices=[('card', 'Credit/debit'), ('ach', 'ACH (Bank transfer)')], max_length=13)),
                ('status', models.CharField(choices=[('cleared', 'Cleared'), ('cancelled', 'Cancelled'), ('denied', 'Denied')], max_length=9)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='billing.Invoice')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

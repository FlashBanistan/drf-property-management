from django.db import models
from uuid import uuid4
from legal.models import Lease
from users.models import Tenant


"""
TODO: 1) Research whether or not 'tax' should be included in amount or
         as a separate field in the Charge model.
      2) Research benefits of 'Billing Package' over individual charges.
      3) Create a 'Credit' model that allows a property manager to
         credit a tenants account.
      4) Create 'Payment' model to track payments received from tenant.
"""

class Payment(models.Model):
    PAYMENT_TYPE_CHOICES = (
        ('card', 'Credit/debit'),
        ('ach', 'ACH (Bank transfer)'),
    )
    PAYMENT_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('partial', 'Partial'),
        ('past_due', 'Past Due'),
        ('cancelled', 'Cancelled'),
        ('denied', 'Denied')
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    created_on = models.DateField(auto_now_add=True)
    payment_type = models.CharField(choices=PAYMENT_TYPE_CHOICES, max_length=13)
    payment_status = models.CharField(choices=PAYMENT_STATUS_CHOICES, max_length=9)
    # Relationships
    paid_by = models.OneToOneField(Tenant)
    lease = models.ForeignKey(Lease, on_delete=models.PROTECT)

class Charge(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    total_amount = models.DecimalField(max_digits=5, decimal_places=2)
    date_due = models.DateField()
    created_on = models.DateField(auto_now_add=True)
    # Relationships
    lease = models.ForeignKey(Lease, on_delete=models.PROTECT)
    payments = models.ForeignKey(Payment, on_delete=models.PROTECT, related_name="charges", null=True, blank=True)
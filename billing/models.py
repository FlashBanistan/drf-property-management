from django.db import models
from uuid import uuid4
from legal.models import Lease
from authentication.models import Tenant


"""
TODO: 1) Research whether or not 'tax' should be included in amount or
         as a separate field in the Charge model.
      2) Research benefits of 'Billing Package' over individual charges.
      3) Create a 'Credit' model that allows a property manager to
         credit a tenants account.
      4) Create 'Payment' model to track payments received from tenant.
"""

class Charge(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    date_due = models.DateField()
    created_on = models.DateField(auto_now_add=True)
    # Relationships
    lease = models.ForeignKey(Lease, on_delete=models.PROTECT)

class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    created_on = models.DateField(auto_now_add=True)
    # Relationships
    paid_by = models.OneToOneField(Tenant)
    charge = models.ForeignKey(Charge, on_delete=models.PROTECT)
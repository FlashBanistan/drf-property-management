from django.db import models
from legal.models import Lease


"""
TODO: 1) Research whether or not 'tax' should be included in amount or
         as a separate field in the Charge model.
      2) Create a 'Credit' model that allows a property manager to
         credit a tenants account.
      3) Create 'Payment' model to track payments received from tenant.
"""

class ChargeType(models.Model):
    name = models.CharField(max_length=255):
    priority = models.PositiveSmallIntegerField(null=True, blank=True)

class Charge(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    date_due = models.DateField()
    created_on = models.DateField(auto_now_add=True)
    # Relationships
    charge_type = models.ForeignKey(ChargeType)
    lease = models.ForeignKey(Lease, on_delete=models.PROTECT)

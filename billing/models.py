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

"""
An invoice is created at the beginning of every billing cycle (after the
previous billing cycle invoice has been processed) and it's status is set
to 'created'. Any charge that is created during the current
billing cycle will be automatically added to the current billing cycle
invoice. 
"""
class Invoice (models.Model):
    INVOICE_STATUS_CHOICES = (
        ('created', 'Created'),
        ('processed', 'Processed'),
        ('charged', 'Charged'),
        ('cancelled', 'Cancelled'),
        ('waived', 'Waived'),
        ('paid_in_full', 'Paid In Full'),
        ('paid_in_part', 'Paid In Part'),
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(choices=INVOICE_STATUS_CHOICES, max_length=12)
    date_created = models.DateField(auto_now_add=True)
    date_processed = models.DateField(null=True, blank=True)
    date_charged = models.DateField(null=True, blank=True)
    date_due = models.DateField(null=True, blank=True)
    paid_in_full_on = models.DateField(null=True, blank=True)
    # Relationships
    lease = models.ForeignKey(Lease, on_delete=models.PROTECT)
    # reverse relationship 'charges'
    # reverse relationship 'payments'
    @property
    def total_charges(self):
        charges = self.charges.all()
        total = 0
        for charge in charges:
            total += charge.amount
        return total

    @property
    def total_payments(self):
        payments = self.payments.filter(status='cleared')
        total = 0
        for payment in payments:
            total += payment.amount
        return total


class Payment(models.Model):
    PAYMENT_TYPE_CHOICES = (
        ('card', 'Credit/debit'),
        ('ach', 'ACH (Bank transfer)'),
    )
    PAYMENT_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('cleared', 'Cleared'),
        ('cancelled', 'Cancelled'),
        ('denied', 'Denied')
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    created_on = models.DateField(auto_now_add=True)
    payment_type = models.CharField(choices=PAYMENT_TYPE_CHOICES, max_length=13)
    status = models.CharField(choices=PAYMENT_STATUS_CHOICES, max_length=9)
    # Relationships
    paid_by = models.ForeignKey(Tenant, on_delete=models.PROTECT)
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT, related_name='payments')

"""
A charge can be created at any point in time. A charge is automatically
added to the current billing cycle's lease.
"""
class Charge(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date_created = models.DateField(auto_now_add=True)
    # Relationships
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT, related_name='charges')
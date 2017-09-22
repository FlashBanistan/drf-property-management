from django.db import models
from legal.models import Lease
from authentication.models import Tenant


class Invoice(models.Model):
    # Relationships:
    lease = models.ForeignKey(Lease)
    tenant = models.ForeignKey(Tenant)

class Charge(models.Model):
    invoice = models.ForeinKey
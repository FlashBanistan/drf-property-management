from django.db import models
from legal.models import Lease
from authentication.models import Tenant


class Invoice(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    # Relationships:
    lease = models.ForeignKey(Lease)
    tenant = models.ForeignKey(Tenant)
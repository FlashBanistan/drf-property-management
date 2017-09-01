from django.db import models
from authentication.models import Tenant
from properties.models import Property, Unit


class Lease(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(editable=False)
    length = models.DurationField(unique=True, help_text='Use the following format: D HH:MM:SS')
    # Relationships:
    leasees = models.ManyToManyField(Tenant)
    leasors = models.ManyToManyField(Property)
    unit = models.OneToOneField(Unit)

    
    def save(self, *args, **kwargs):
        print('Length: ', self.length)
        print('End date: ', self.start_date + self.length)
        self.end_date = self.start_date + self.length
        super(Lease, self).save(*args, **kwargs)
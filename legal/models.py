from django.db import models
from property_management.models import CommonModel

class Lease(CommonModel):
    start_date = models.DateField()
    end_date = models.DateField()
    # Relationships:
    # complex = models.ForeignKey('real_estate.Complex')
    unit = models.OneToOneField('real_estate.Unit', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.unit.address + ' ' + self.unit.city + ' ' + self.unit.state + ' #' + self.unit.unit_number
    
    # def save(self, *args, **kwargs):
    #     super(Lease, self).save(*args, **kwargs)
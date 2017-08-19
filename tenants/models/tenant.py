from django.db import models
from properties.models.unit import Unit
from tenants.models.occupant_type import OccupantType
from property_management.validators.phone_number import validate_phone_number

"""
Model fields default to required.  To make a field optional add, 'null=True'. 
Left side of CHOICES tuple is saved to database; right side is the human-readable form.
"""
class Tenant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=11, validators=[validate_phone_number], null=True, blank=True)
    ssn = models.CharField(max_length=11, null=True, blank=True)
    # Relationships:
    occupant_type = models.ForeignKey(OccupantType, null=True, on_delete=models.SET_NULL)
    unit = models.ForeignKey(Unit, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

from django.db import models
from properties.models.unit import Unit
from property_management.validators.phone_number import validate_phone_number

class Tenant(models.Model):
    OCCUPANT_TYPE_CHOICES = (
        ('primary', 'Primary'),
        ('occupant', 'Occupant'),
    )
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone_number = models.CharField(max_length=11, validators=[validate_phone_number], null=False, blank=False)
    ssn = models.CharField(max_length=11)
    occupant_type = models.CharField(max_length=100, choices=OCCUPANT_TYPE_CHOICES)
    # Relationships:
    unit = models.ForeignKey(Unit, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
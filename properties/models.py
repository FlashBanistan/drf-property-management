from django.db import models
from authentication.models import Tenant
from property_management.validators.phone_number import validate_phone_number

class Property(models.Model):
    # Identification details:
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11, validators=[validate_phone_number])
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    # Relationships:
    tenants = models.ForeignKey(Tenant, null=True, blank=True, on_delete=models.SET_NULL)
    # Other details:
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Properties"


class Building(models.Model):
    name = models.CharField(max_length=100)
    # Relationships:
    property = models.ForeignKey(Property, null=True, blank=True, on_delete=models.CASCADE)
    tenants = models.ForeignKey(Tenant, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Unit(models.Model):
    # Location details:
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    unit_number = models.CharField(max_length=10, default=None)
    # Unit details:
    sq_ft = models.IntegerField(null=True, blank=True)
    bedrooms = models.IntegerField(null=True, blank=True)
    baths = models.FloatField(null=True, blank=True)
    # Relationships:
    property = models.ForeignKey(Property, null=True, blank=True, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, null=True, blank=True, on_delete=models.SET_NULL)
    tenants = models.ForeignKey(Tenant, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return 'Unit ' + self.unit_number
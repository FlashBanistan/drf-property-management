from django.db import models
from property_management.validators.phone_number import validate_phone_number

class Complex(models.Model):
    """ Reverse Relationship Fields(buildings, units, tenants) """
    # Identification details:
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11, validators=[validate_phone_number])
    email = models.EmailField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    # Relationships:
    # Other details:
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Complexes"


class Building(models.Model):
    """ Reverse Relationship Fields(units, tenants) """
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    # Relationships:
    complex = models.ForeignKey(Complex, null=True, blank=True, on_delete=models.CASCADE, related_name='buildings')

    def __str__(self):
        return self.name


class Unit(models.Model):
    """ Reverse Relationship Fields(tenants) """
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
    complex = models.ForeignKey(Complex, null=True, blank=True, on_delete=models.CASCADE, related_name='units')
    building = models.ForeignKey(Building, null=True, blank=True, on_delete=models.SET_NULL, related_name='units')

    def __str__(self):
        return 'Unit ' + self.unit_number
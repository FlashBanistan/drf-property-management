from django.db import models
from property_management.validators.phone_number import validate_phone_number

class Property(models.Model):
    # Identification details:
    name = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=11, validators=[validate_phone_number])
    address = models.CharField(max_length=100, null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    state = models.CharField(max_length=100, null=False, blank=False)
    zip_code = models.CharField(max_length=10,null=False, blank=False)
    # Relationships:
    
    # Other details:
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Properties"


class Building(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    # Relationships:
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Unit(models.Model):
    # Location details:
    address = models.CharField(max_length=100, null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    state = models.CharField(max_length=100, null=False, blank=False)
    zip_code = models.CharField(max_length=10,null=False, blank=False)
    unit_number = models.CharField(max_length=10, default=None)
    # Unit details:
    sq_ft = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.FloatField()
    # Relationships:
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return 'Unit ' + self.unit_number
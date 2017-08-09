from django.db import models
from properties.models.building import Building
from clients.models import Client
from properties.models.property import Property

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
    # client = models.ForeignKey(Client, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return 'Unit ' + self.unit_number
from django.db import models
from properties.models.property import Property

class Building(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    # Relationships:
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
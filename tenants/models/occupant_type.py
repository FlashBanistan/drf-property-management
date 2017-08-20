from django.db import models

"""
Consider removing 'primary_key=True' so as to allow for future model
instances without screwing up the odering.
"""
class OccupantType(models.Model):
    name = models.CharField(max_length=100)
    occupant_type_id = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.occupant_type_id) + ' - ' + self.name
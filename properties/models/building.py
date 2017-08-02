from django.db import models
from clients.models import Client

class Building(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    # Relationships:
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
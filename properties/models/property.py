from django.db import models
from clients.models import Client
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
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    # Other details:
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Properties"

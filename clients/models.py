from django.db import models
from property_management.validators.phone_number import validate_phone_number
from property_management.models import CommonModel

class Client(CommonModel):
    # Identifaction details:
    name = models.CharField(max_length=100)
    # owner = models.CharField(max_length=100)
    # email = models.EmailField(max_length=100)
    # phone = models.CharField(max_length=11, validators=[validate_phone_number])
    # Location details:
    # address = models.CharField(max_length=100, null=False, blank=False)
    # city = models.CharField(max_length=100, null=False, blank=False)
    # state = models.CharField(max_length=100, null=False, blank=False)
    # zip_code = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return self.name
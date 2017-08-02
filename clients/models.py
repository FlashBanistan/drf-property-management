from django.db import models
from tenant_schemas.models import TenantMixin
from property_management.validators.phone_number import validate_phone_number

class Client(TenantMixin):
    # Identifaction details:
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=11, validators=[validate_phone_number])
    # Location details:
    address = models.CharField(max_length=100, null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    state = models.CharField(max_length=100, null=False, blank=False)
    zip_code = models.CharField(max_length=10, null=False, blank=False)
    # Other details:
    created_on = models.DateField(auto_now_add=True)

    # Default true, schema will be automatically created and synced when it is saved.
    auto_create_schema = True

    def __str__(self):
        return self.name
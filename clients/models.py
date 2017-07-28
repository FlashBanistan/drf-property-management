from django.db import models
from tenant_schemas.models import TenantMixin
from property_management.validators.phone_number import validate_phone_number

class Client(TenantMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=11, validators=[validate_phone_number])
    created_on = models.DateField(auto_now_add=True)

    # Default true, schema will be automatically created and synced when it is saved.
    auto_create_schema = True

    def __str__(self):
        return self.name
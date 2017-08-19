from django.contrib import admin
from tenants.models.tenant import Tenant
from tenants.models.occupant_type import OccupantType

admin.site.register(Tenant)
admin.site.register(OccupantType)

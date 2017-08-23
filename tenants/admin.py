from django.contrib import admin
from tenants.models import Tenant
from tenants.models import OccupantType

admin.site.register(Tenant)
admin.site.register(OccupantType)

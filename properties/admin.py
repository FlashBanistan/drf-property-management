from django.contrib import admin
from properties.models.unit import Unit
from properties.models.building import Building

admin.site.register(Unit)
admin.site.register(Building)
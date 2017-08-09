from django.contrib import admin
from properties.models import Unit
from properties.models import Building
from properties.models import Property

admin.site.register(Unit)
admin.site.register(Building)
admin.site.register(Property)
from django.contrib import admin
from real_estate.models import Unit
from real_estate.models import Building
from real_estate.models import Complex

admin.site.register(Unit)
admin.site.register(Building)
admin.site.register(Complex)
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import BuildingSerializer, UnitSerializer
from .models.building import Building
from .models.unit import Unit

User = get_user_model()

class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = (
        'id',
        'name'
    )


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = (
        'address',
        'baths',
        'bedrooms',
        'city',
        'id',
        'sq_ft',
        'state',
        'unit_number',
        'zip_code'
    )
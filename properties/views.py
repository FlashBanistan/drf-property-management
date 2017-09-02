from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import BuildingSerializer, UnitSerializer, UnitBulkCreateSerializer, PropertySerializer
from .models import Property, Building, Unit

User = get_user_model()

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = (
        'id',
        'name'
    )

    @list_route(methods=['post'])
    def bulk_create(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = (
        'id',
        'name'
    )

    @list_route(methods=['post'])
    def bulk_create(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

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

    @list_route(methods=['post'])
    def bulk_create(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
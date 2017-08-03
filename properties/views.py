from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import BuildingSerializer, UnitSerializer
from .models.building import Building
from .models.unit import Unit

User = get_user_model()

class BuildingViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Building.objects.all()
        serializer = BuildingSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Building.objects.all()
        building = get_object_or_404(queryset, pk=pk)
        serializer = BuildingSerializer(building)
        return Response(serializer.data)

    def create(self, request):
        serializer = BuildingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        queryset = Building.objects.all()
        building = get_object_or_404(queryset, pk=pk)
        serializer = BuildingSerializer(building, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def partial_update(self, request, pk=None):
        queryset = Building.objects.all()
        building = get_object_or_404(queryset, pk=pk)
        serializer = BuildingSerializer(building, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        queryset = Building.objects.all()
        building = get_object_or_404(queryset, pk=pk)
        building.delete()
        return Response(status=201)


class UnitViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Unit.objects.all()
        serializer = UnitSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Unit.objects.all()
        unit = get_object_or_404(queryset, pk=pk)
        serializer = UnitSerializer(unit)
        return Response(serializer.data)

    def create(self, request):
        serializer = UnitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        queryset = Unit.objects.all()
        unit = get_object_or_404(queryset, pk=pk)
        serializer = UnitSerializer(unit, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def partial_update(self, request, pk=None):
        queryset = Unit.objects.all()
        unit = get_object_or_404(queryset, pk=pk)
        serializer = UnitSerializer(unit, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        queryset = Unit.objects.all()
        unit = get_object_or_404(queryset, pk=pk)
        unit.delete()
        return Response(status=201)
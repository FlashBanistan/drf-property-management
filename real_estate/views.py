from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from clients.views import ClientAwareViewSet
from .serializers import (
    BuildingSerializer,
    BuildingDetailSerializer,
    UnitSerializer,
    UnitBulkCreateSerializer,
    ComplexSerializer,
    ComplexDetailSerializer,
)
from .models import Complex, Building, Unit


class ComplexViewSet(ClientAwareViewSet):
    queryset = Complex.objects.all()
    # serializer_class = ComplexSerializer
    filter_fields = "__all__"
    ordering_fields = "__all__"
    search_fields = ("id", "name")

    def get_serializer_class(self):
        if self.action == "list":
            return ComplexSerializer
        if self.action == "retrieve":
            return ComplexDetailSerializer
        return ComplexSerializer  # Add create/destroy/update.

    @action(methods=["post"], detail=False)
    def bulk_create(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


class BuildingViewSet(ClientAwareViewSet):
    queryset = Building.objects.all()
    # serializer_class = BuildingSerializer
    filter_fields = "__all__"
    ordering_fields = "__all__"
    search_fields = ("id", "name")

    def get_serializer_class(self):
        if self.action == "list":
            return BuildingSerializer
        if self.action == "retrieve":
            return BuildingDetailSerializer
        if self.action == "update":
            return BuildingDetailSerializer
        return BuildingSerializer  # Add create/destroy/update.

    @action(methods=["post"], detail=False)
    def bulk_create(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


class UnitViewSet(ClientAwareViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    filter_fields = "__all__"
    ordering_fields = "__all__"
    search_fields = (
        "address",
        "baths",
        "bedrooms",
        "city",
        "id",
        "sq_ft",
        "state",
        "unit_number",
        "zip_code",
    )

    @action(methods=["post"], detail=False)
    def bulk_create(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

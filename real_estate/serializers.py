from rest_framework.serializers import HyperlinkedModelSerializer, ListSerializer
from .models import Complex, Building, Unit

class ComplexBulkCreateSerializer(ListSerializer):
    def create(self, validated_data):
        properties = [Complex(**_Complex) for _Complex in validated_data]
        return Complex.objects.bulk_create(properties)

class ComplexSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Complex
        list_serializer_class = ComplexBulkCreateSerializer
        fields = (
            'url', 'name', 'phone', 'email', 'address',
            'city', 'state', 'zip_code',
        )

class ComplexDetailSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Complex
        list_serializer_class = ComplexBulkCreateSerializer
        fields = (
            'url', 'name', 'phone', 'email', 'address',
            'city', 'state', 'zip_code', 'buildings',
            'units', 'tenants',
        )

class BuildingBulkCreateSerializer(ListSerializer):
    def create(self, validated_data):
        buildings = [Building(**building) for building in validated_data]
        return Building.objects.bulk_create(buildings)

class BuildingSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Building
        list_serializer_class = BuildingBulkCreateSerializer
        fields = (
            'url', 'name', 'address', 'city',
            'state', 'zip_code'
        )

class BuildingDetailSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Building
        list_serializer_class = BuildingBulkCreateSerializer
        fields = (
            'url', 'name', 'address', 'city',
            'state', 'zip_code', 'Complex',
            'tenants',
        )

class UnitBulkCreateSerializer(ListSerializer):
    def create(self, validated_data):
        units = [Unit(**unit) for unit in validated_data]
        return Unit.objects.bulk_create(units)

class UnitSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Unit
        list_serializer_class = UnitBulkCreateSerializer
        fields = [
            'url', 'address', 'city', 'state',
            'zip_code', 'unit_number', 'sq_ft',
            'bedrooms', 'baths', 'Complex','building',
            'tenants',
        ]
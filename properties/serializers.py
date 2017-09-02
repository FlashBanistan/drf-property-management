from rest_framework.serializers import HyperlinkedModelSerializer, ListSerializer
from .models import Property, Building, Unit

class PropertyBulkCreateSerializer(ListSerializer):
    def create(self, validated_data):
        properties = [Property(**_property) for _property in validated_data]
        return Property.objects.bulk_create(properties)

class PropertySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Property
        list_serializer_class = PropertyBulkCreateSerializer
        fields = '__all__'

class BuildingBulkCreateSerializer(ListSerializer):
    def create(self, validated_data):
        buildings = [Building(**building) for building in validated_data]
        return Building.objects.bulk_create(buildings)

class BuildingSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Building
        list_serializer_class = BuildingBulkCreateSerializer
        fields = '__all__'

class UnitBulkCreateSerializer(ListSerializer):
    def create(self, validated_data):
        units = [Unit(**unit) for unit in validated_data]
        return Unit.objects.bulk_create(units)

class UnitSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Unit
        list_serializer_class = UnitBulkCreateSerializer
        fields = [
            'url',
            'address',
            'city',
            'state',
            'zip_code',
            'unit_number',
            'sq_ft',
            'bedrooms',
            'baths',
            'property',
            'building',
            'tenants'
        ]
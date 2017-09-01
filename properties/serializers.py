from rest_framework.serializers import HyperlinkedModelSerializer, ListSerializer
from .models import Property, Building, Unit

class PropertySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class BuildingSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'

class UnitBulkCreateSerializer(ListSerializer):
    def create(self, validated_data):
        units = [Unit(**item) for item in validated_data]
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
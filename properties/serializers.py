from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Property, Building, Unit

class PropertySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class BuildingSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'

class UnitSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'
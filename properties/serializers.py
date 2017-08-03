from rest_framework.serializers import ModelSerializer
from .models import Building, Unit

class BuildingSerializer(ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'

class UnitSerializer(ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'
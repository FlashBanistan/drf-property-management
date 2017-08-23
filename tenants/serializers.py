from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Tenant, OccupantType


class OccupantTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = OccupantType
        fields = '__all__'

class TenantSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Tenant
        fields = [
            'url',
            'occupant_type',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'ssn',
            'unit',
        ]
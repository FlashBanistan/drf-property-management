from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Lease
from authentication.serializers import TenantListSerializer
from properties.serializers import PropertySerializer, UnitSerializer


class LeaseListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Lease
        fields = [
            'url',
            'start_date',
            'end_date',
            'property_owner',
            'unit',
            'tenant_set'
        ]


class LeaseDetailSerializer(HyperlinkedModelSerializer):
    tenant_set = TenantListSerializer(many=True)
    property_owner = PropertySerializer()
    unit = UnitSerializer()
    class Meta:
        model = Lease
        fields = [
            'start_date',
            'end_date',
            'property_owner',
            'unit',
            'tenant_set' 
        ]

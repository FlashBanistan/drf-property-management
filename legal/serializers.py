from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Lease
from users.serializers import TenantListSerializer
from real_estate.serializers import ComplexSerializer, UnitSerializer


class LeaseListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Lease
        fields = [
            'url',
            'start_date',
            'end_date',
            # 'complex',
            'unit',
            'tenants'
        ]


class LeaseDetailSerializer(HyperlinkedModelSerializer):
    tenant_set = TenantListSerializer(many=True)
    # complex = ComplexSerializer()
    unit = UnitSerializer()
    class Meta:
        model = Lease
        fields = [
            'start_date',
            'end_date',
            # 'complex',
            'unit',
            'tenants' 
        ]

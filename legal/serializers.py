from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Lease
from authentication.serializers import TenantListSerializer


class LeaseListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Lease
        fields = [
            'url',
            'start_date',
            'end_date',
            'lessor',
            'unit',
            'tenant_set'
        ]


class LeaseDetailSerializer(HyperlinkedModelSerializer):
    tenant_set = TenantListSerializer(many=True)
    class Meta:
        model = Lease
        fields = [
            'start_date',
            'end_date',
            'lessor',
            'unit',
            'tenant_set'
        ]
        depth = 1
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Lease
from authentication.serializers import TenantSerializer


class LeaseListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Lease
        fields = '__all__'


class LeaseDetailSerializer(HyperlinkedModelSerializer):
    tenant_set = TenantSerializer(many=True)
    class Meta:
        model = Lease
        fields = [
            'url',
            'pk',
            'start_date',
            'end_date',
            'lessor',
            'unit',
            'tenant_set'
        ]
        depth = 1
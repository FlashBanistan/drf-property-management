from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Tenant, TenantType


class TenantTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = TenantType
        fields = '__all__'

class TenantSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Tenant
        fields = [
            'url',
            'tenant_type',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'ssn',
        ]
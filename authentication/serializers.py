from rest_framework.serializers import HyperlinkedModelSerializer, ListSerializer, EmailField
from .models import Tenant, TenantType


class TenantTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = TenantType
        fields = '__all__'

class TenantBulkCreateSerializer(ListSerializer):
    def create(self, validated_data):
        tenants = [Tenant(**tenant) for tenant in validated_data]
        return Tenant.objects.bulk_create(tenants)

class TenantSerializer(HyperlinkedModelSerializer):
    email = EmailField(required=False)
    class Meta:
        model = Tenant
        list_serializer_class = TenantBulkCreateSerializer
        fields = [
            'url',
            'tenant_type',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'ssn',
        ]
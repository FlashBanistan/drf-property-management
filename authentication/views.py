from rest_framework import viewsets
from .serializers import TenantSerializer, TenantTypeSerializer
from .models import Tenant, TenantType


class OccupantTypeViewSet(viewsets.ModelViewSet):
    queryset = TenantType.objects.all()
    serializer_class = TenantTypeSerializer
    
class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = (
        'email',
        'first_name',
        'id',
        'last_name',
        'tenant_type',
        'phone_number',
        'ssn'
    )
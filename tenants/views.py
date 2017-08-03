from rest_framework import viewsets
from .serializers import TenantSerializer
from .models import Tenant


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
        'occupant_type',
        'phone_number',
        'ssn'
    )
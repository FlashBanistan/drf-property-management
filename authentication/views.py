from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework import status
from .serializers import TenantListSerializer, TenantTypeSerializer, AuthUserSerializer
from .models import Tenant, TenantType, AuthUser

class AuthUserViewSet(viewsets.ModelViewSet):
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer

class TenantTypeViewSet(viewsets.ModelViewSet):
    queryset = TenantType.objects.all()
    serializer_class = TenantTypeSerializer
    
class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantListSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = (
        'auth',
        'first_name',
        'id',
        'last_name',
        'tenant_type',
        'phone_number',
        'ssn'
    )

    @list_route(methods=['post'])
    def bulk_create(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
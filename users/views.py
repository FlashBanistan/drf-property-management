from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from clients.views import ClientAwareViewSet
from .serializers import (
    TenantListSerializer,
    TenantDetailSerializer,
    AuthUserSerializer,
    AdminSerializer,
)
from .models import Tenant, AuthUser, Admin


class AuthUserViewSet(ClientAwareViewSet):
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer


class AdminViewSet(ClientAwareViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    # serializer_class = TenantListSerializer
    filter_fields = "__all__"
    ordering_fields = "__all__"
    search_fields = ("first_name", "id", "last_name", "phone_number", "ssn")

    def get_serializer_class(self):
        if self.action == "list":
            return TenantListSerializer
        if self.action == "retrieve":
            return TenantDetailSerializer
        if self.action == "update":
            return TenantDetailSerializer
        return TenantListSerializer  # Add create/destroy.

    @action(methods=["post"], detail=False)
    def bulk_create(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

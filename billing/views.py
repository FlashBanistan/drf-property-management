from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from .models import Charge, Payment, Invoice


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = (
        'id'
    )

    def get_serializer_class(self):
        if self.action == 'list':
            return PaymentListSerializer
        if self.action == 'retrieve':
            return PaymentListSerializer
        if self.action == 'create':
            return PaymentCreateSerializer
        if self.action == 'update':
            return PaymentUpdateSerializer
        return PaymentListSerializer # Add destroy
    
    # Modify request to include fields not sent back from frontend.
    def perform_create(self, serializer):
        serializer.save(paid_by=self.request.user.tenant)
            

class ChargeViewSet(viewsets.ModelViewSet):
    queryset = Charge.objects.all()
    serializer_class = ChargeListSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = (
        'id', 'name', 'date_created', 'date_processed',
        'date_charged', 'date_due', 'paid_in_full_on',
        'lease', 'payments',    
    )

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    # serializer_class = InvoiceListSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = (
        'id', 'description', 'invoice_status', 'date_created'
        'date_processed', 'date_charged', 'date_due', 'paid_in_full_on',
        'lease'
    )

    def get_serializer_class(self):
        if self.action == 'list':
            return InvoiceListSerializer
        if self.action == 'retrieve':
            return InvoiceDetailSerializer
        return InvoiceListSerializer # Add create/destroy/update.
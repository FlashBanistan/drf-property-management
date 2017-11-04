from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ChargeListSerializer, PaymentListSerializer
from .models import Charge, Payment


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    # serializer_class = PaymentListSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = (
        'id'
    )

    def get_serializer_class(self):
        if self.action == 'list':
            return PaymentListSerializer
        if self.action =='retrieve':
            return PaymentListSerializer
        return PaymentListSerializer # Add create/destroy/update.

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
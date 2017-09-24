from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ChargeSerializer, PaymentSerializer
from .models import Charge, Payment


class ChargeViewSet(viewsets.ModelViewSet):
    queryset = Charge.objects.all()
    serializer_class = ChargeSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = (
        'id',
        'name'
    )

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = (
        'id'
    )
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Charge, Payment

class PaymentListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class ChargeListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Charge
        fields = (
            'url', 'name', 'description', 'total_amount',
            'charge_status', 'date_created', 'date_processed',
            'date_charged', 'date_due', 'paid_in_full_on', 'lease',
            'payments',
        )

class ChargeDetailSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Charge
        payments = PaymentListSerializer(many=True)
        fields = (
            'url', 'name', 'description', 'total_amount',
            'charge_status', 'date_created', 'date_processed',
            'date_charged', 'date_due', 'paid_in_full_on', 'lease',
            'payments',
        )

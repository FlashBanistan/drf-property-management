from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField, ValidationError, ReadOnlyField, CurrentUserDefault
from .models import Charge, Payment, Invoice

class PaymentListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'url', 'amount', 'created_on', 'payment_type',
            'status', 'paid_by', 'invoice',
        )

class PaymentDetailSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'url', 'amount', 'created_on', 'payment_type',
            'status', 'paid_by', 'invoice',
        )

class PaymentUpdateSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'amount', 'payment_type',
        )

class PaymentCreateSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        paid_by = CurrentUserDefault()
        fields = (
            'amount', 'payment_type', 'invoice', 'paid_by'
        )
        read_only_fields = ('paid_by',)

class ChargeListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Charge
        fields = (
            'url', 'name', 'description', 'amount',
            'date_created', 'invoice',
        )

class ChargeDetailSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Charge
        payments = PaymentListSerializer(many=True)
        fields = (
            'url', 'name', 'description', 'amount',
            'date_created', 'invoice',
        )


class InvoiceListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Invoice
        fields = (
            'url', 'description', 'status', 'date_created',
            'date_processed', 'date_charged', 'date_due', 'paid_in_full_on',
            'payments', 'lease', 'charges'
        )

class InvoiceDetailSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Invoice
        fields = (
            'url', 'total_charges', 'total_payments', 'description',
            'status', 'date_created', 'date_processed', 'date_charged',
            'date_due', 'paid_in_full_on', 'payments', 'lease',
            'charges'
        )

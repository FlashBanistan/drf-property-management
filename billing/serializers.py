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
            'status',
        )

class PaymentCreateSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        paid_by = CurrentUserDefault()
        fields = (
            'amount', 'payment_type', 'invoice', 'paid_by', 'status',
        )
        read_only_fields = ('paid_by',)
    
    def validate(self, data):
        if data['status'] != 'cleared':
            raise ValidationError("A payment must be set to 'cleared' at the time of creation.")
        total_charges = data['invoice'].total_charges
        total_payments = data['invoice'].total_payments
        if data['amount'] > (total_charges - total_payments):
            raise ValidationError('You cannot pay more than you owe.')
        return data


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

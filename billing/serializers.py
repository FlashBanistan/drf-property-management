from rest_framework import serializers
from .models import Charge, Payment, Invoice



""""""""""""""""""""""" PAYMENT SERIALIZERS """""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class PaymentListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'url',
            'amount',
            'created_on',
            'payment_type',
            'status',
            'paid_by',
            'invoice',
        )

class PaymentDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'url',
            'amount',
            'created_on',
            'payment_type',
            'status',
            'paid_by',
            'invoice',
        )

class PaymentUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'status',
        )

class PaymentCreateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        paid_by = serializers.CurrentUserDefault()
        fields = (
            'amount',
            'payment_type',
            'invoice',
            'paid_by',
            'status',
        )
        read_only_fields = ('paid_by',)
    
    def validate(self, data):
        if data['status'] != 'cleared':
            raise ValidationError("A payment must be set to 'cleared' at the time of creation.")
        if data['invoice'].status != 'charged':
            raise ValidationError("The invoice must be charged before payments can be accepted for it.")
        total_charges = data['invoice'].total_charges
        total_payments = data['invoice'].total_payments
        if data['amount'] > (total_charges - total_payments):
            raise ValidationError('You cannot pay more than you owe.')
        return data

class PaymentDestroySerializer(serializers.HyperlinkedModelSerializer):
    pass



""""""""""""""""""""""" CHARGE SERIALIZERS """"""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class ChargeListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Charge
        fields = (
            'url',
            'name',
            'description',
            'amount',
            'date_created',
            'invoice',
        )

class ChargeDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Charge
        fields = (
            'url',
            'name',
            'description',
            'amount',
            'date_created',
            'invoice',
        )

class ChargeCreateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Charge
        fields = (
            'name',
            'description',
            'amount',
            'date_created',
        )

class ChargeUpdateSerializer(serializers.HyperlinkedModelSerializer):
    pass

class ChargeDestroySerializer(serializers.HyperlinkedModelSerializer):
    pass



""""""""""""""""""""""" INVOICE SERIALIZERS """""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class InvoiceListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoice
        fields = (
            'url',
            'description',
            'status',
            'date_created',
            'date_processed',
            'date_charged',
            'date_due',
            'paid_in_full_on',
            'payments',
            'lease',
            'charges'
        )

class InvoiceDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoice
        fields = (
            'url',
            'total_charges',
            'total_payments',
            'description',
            'status',
            'date_created',
            'date_processed',
            'date_charged',
            'date_due',
            'paid_in_full_on',
            'payments',
            'lease',
            'charges',
        )

class InvoiceCreateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoice
        fields = (
            'description',
            'status',
            'date_created',
            'date_due',
            'lease',
            'url'
        )
    def create(self, validated_data):
        charges = Charge.objects.filter(invoice=None)
        if not charges.exists():
            raise ValidationError('There are no charges to assign to an invoice at this time.')
        invoice = Invoice(**validated_data)
        invoice.save()
        for charge in charges:
            charge.invoice = invoice
            charge.save()
        return invoice

class InvoiceUpdateSerializer(serializers.HyperlinkedModelSerializer):
    pass

class InvoiceDestroySerializer(serializers.HyperlinkedModelSerializer):
    pass

from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime 

@receiver(post_save, sender=Payment)
def save_user_profile(sender, instance, **kwargs):
    if instance.invoice.total_payments == instance.invoice.total_charges:
        instance.invoice.paid_in_full_on = datetime.now()
        instance.invoice.save()

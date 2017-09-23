from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Charge, Payment

class ChargeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Charge
        fields = '__all__'

class PaymentSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = '_all__'
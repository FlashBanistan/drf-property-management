from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Charge, Payment

class ChargeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Charge
        fields = '__all__'

class PaymentListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
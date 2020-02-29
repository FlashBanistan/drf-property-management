from rest_framework import serializers
from .models import CommonModel



""""""""""""""""""""""" COMMON SERIALIZERS """""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class CommonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'url',
            'id',
            'date_created',
            'date_updated',
        )
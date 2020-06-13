from rest_framework import serializers
from .models import CommonModel



""""""""""""""""""""""" COMMON SERIALIZERS """""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class CommonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CommonModel
        fields = (
            'url',
            'id',
            'date_created',
            'date_updated',
        )
        abstract = True
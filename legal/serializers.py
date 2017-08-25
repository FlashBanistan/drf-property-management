from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Lease


class LeaseSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Lease
        fields = '__all__'

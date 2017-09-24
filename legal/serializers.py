from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Lease


class LeaseListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Lease
        fields = '__all__'


class LeaseDetailSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Lease
        fields = '__all__'
        depth = 1
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Lease
from users.serializers import UserReadSerializer


class LeaseListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Lease
        fields = ["url", "start_date", "end_date", "unit", "tenants"]


class LeaseDetailSerializer(HyperlinkedModelSerializer):
    tenants = UserReadSerializer(many=True)

    class Meta:
        model = Lease
        fields = ["start_date", "end_date", "unit", "tenants"]

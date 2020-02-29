from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Tenant


class TenantSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Tenant
        fields = [
            'url',
            'name',
            'email',
            'phone',
        ]

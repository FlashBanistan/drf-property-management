from rest_framework import viewsets
from .serializers import LeaseSerializer
from .models import Lease


class LeaseViewSet(viewsets.ModelViewSet):
    queryset = Lease.objects.all()
    serializer_class = LeaseSerializer
    # filter_fields = '__all__'
    # ordering_fields = '__all__'
    # search_fields = (
    # 
    # )
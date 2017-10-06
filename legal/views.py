from rest_framework import viewsets
from .serializers import LeaseListSerializer, LeaseDetailSerializer
from .models import Lease


class LeaseViewSet(viewsets.ModelViewSet):
    queryset = Lease.objects.all()
    # serializer_class = LeaseListSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    # search_fields = (
    # 
    # )

    def get_serializer_class(self):
        if self.action == 'list':
            return LeaseListSerializer
        if self.action == 'retrieve':
            return LeaseDetailSerializer
        return LeaseListSerializer # Add create/destroy/update.               
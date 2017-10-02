from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import AnnouncementSerializer, MaintenanceRequestSerializer
from .models import Announcement, MaintenanceRequest

"""
Order by created_on and limit.
"""

class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = (
        'title'
    )

class MaintenanceRequestViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceRequest.objects.all()
    serializer_class = MaintenanceRequestSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = (
        'created_on'
    )
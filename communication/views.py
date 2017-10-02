from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import AnnouncementSerializer
from .models import Announcement

"""
Order by created_on and limit.
"""

class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    filter_fields = '__all__'
    ordering_fieldds = '__all__'
    search_fields = (
        'title'
    )
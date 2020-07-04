from rest_framework import viewsets
from rest_framework.response import Response
from clients.views import ClientAwareViewSet
from property_management.utils import user_from_request
from .serializers import AnnouncementSerializer, MaintenanceRequestSerializer
from .models import Announcement, MaintenanceRequest

"""
Order by created_on and limit.
"""


class AnnouncementViewSet(ClientAwareViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    filter_fields = ("title", "body")
    ordering_fields = ("title", "body")
    search_fields = ("title",)


class MaintenanceRequestViewSet(ClientAwareViewSet):
    queryset = MaintenanceRequest.objects.all()
    serializer_class = MaintenanceRequestSerializer
    filter_fields = ("description", "permission_to_enter", "date_created", "created_by")
    ordering_fields = (
        "description",
        "permission_to_enter",
        "date_created",
        "created_by",
    )
    search_fields = "date_created"

    def perform_create(self, serializer, *args, **kwargs):
        user = user_from_request(self.request)
        serializer.save(created_by=user, **kwargs)
        super(MaintenanceRequestViewSet, self).perform_create(
            serializer, *args, **kwargs
        )

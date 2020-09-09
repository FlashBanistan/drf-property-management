from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Announcement, MaintenanceRequest


class AnnouncementSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Announcement
        fields = ("url", "id", "title", "body", "date_created", "date_updated")
        read_only_fields = ("id",)


class MaintenanceRequestSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = MaintenanceRequest
        fields = (
            "url",
            "id",
            "description",
            "permission_to_enter",
            "photo",
            "status",
            "date_completed",
            "date_created",
            "date_updated",
        )
        read_only_fields = (
            "id",
            "status",
        )

from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Announcement, MaintenanceRequest


class AnnouncementSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'

class MaintenanceRequestSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = MaintenanceRequest
        fields = '__all__'
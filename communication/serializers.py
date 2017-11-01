from rest_framework.serializers import HyperlinkedModelSerializer, CurrentUserDefault
from .models import Announcement, MaintenanceRequest


class AnnouncementSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'

class MaintenanceRequestSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = MaintenanceRequest
        created_by = CurrentUserDefault()
        fields = (
            'url',
            'description',
            'permission_to_enter',
            'photo',
            'created_on',
            'created_by',
        )
        # def save(self):
        #     created_by = CurrentUserDefault()
from rest_framework.serializers import HyperlinkedModelSerializer, CurrentUserDefault, BooleanField
from .models import Announcement, MaintenanceRequest
from property_management.serializers import CommonSerializer


class AnnouncementSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'

class MaintenanceRequestSerializer(CommonSerializer):
    class Meta:
        model = MaintenanceRequest
        created_by = CurrentUserDefault()
        fields = (
            'url',
            'description',
            'permission_to_enter',
            'photo',
            'date_created',
            'created_by',
        )
        # def save(self):
        #     created_by = CurrentUserDefault()
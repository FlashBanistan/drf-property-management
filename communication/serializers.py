from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Announcement


class AnnouncementSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'
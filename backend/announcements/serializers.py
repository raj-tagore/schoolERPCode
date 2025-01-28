from rest_framework import serializers
from .models import Announcement
from accounts.serializers import TeacherSerializer

class AnnouncementSerializer(serializers.ModelSerializer):
    signed_by_details = TeacherSerializer(source='signed_by', read_only=True)
    class Meta:
        model = Announcement
        fields = '__all__'



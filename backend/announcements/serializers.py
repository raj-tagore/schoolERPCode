from rest_framework import serializers
from .models import Announcement
from accounts.serializers import TeacherSerializer

class AnnouncementSerializer(serializers.ModelSerializer):
    signed_by = TeacherSerializer(required=False)
    class Meta:
        model = Announcement
        fields = '__all__'



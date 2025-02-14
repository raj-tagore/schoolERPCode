from rest_framework import serializers
from .models import Event
from accounts.serializers import TeacherSerializer

class EventSerializer(serializers.ModelSerializer):
    created_by_details = TeacherSerializer(source='created_by', read_only=True)
    
    class Meta:
        model = Event
        fields = ["id", "title", "start", "end", "description", "classrooms", 
                  "subjects", "is_school_wide", "attachment", "created_by", "created_by_details"]



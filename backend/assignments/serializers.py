from rest_framework import serializers
from .models import Assignment, SubmittedAssignment
from allocation.serializers import SubjectSerializer

class AssignmentSerializer(serializers.ModelSerializer):
    subject_details = SubjectSerializer(source='subject', read_only=True)
    class Meta:
        model = Assignment
        fields = [
            "id",
            "title",
            "description",
            "is_active",
            "release_at",
            "due_at",
            "subject",
            "subject_details",
        ]

class BasicAssignmentSerializer(serializers.ModelSerializer):
    subject_details = SubjectSerializer(source='subject', read_only=True)
    class Meta:
        model = Assignment
        fields = [
            "id",
            "title",
            "description",
            "is_active",
            "release_at",
            "due_at",
            "subject",
            "subject_details",
        ]

class SubmittedAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmittedAssignment
        fields = [
            "id",
            "student",
            "assignment",
            "status",
            "submission_datetime",
        ]

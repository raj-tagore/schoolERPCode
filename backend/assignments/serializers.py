from rest_framework import serializers
from .models import Assignment, SubmittedAssignment


class AssignmentSerializer(serializers.ModelSerializer):
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
        ]


class BasicAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = [
            "id",
            "title",
            "is_active",
            "release_at",
            "due_at",
            "subject",
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

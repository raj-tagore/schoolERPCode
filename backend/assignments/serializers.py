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
            "release_datetime",
            "due_datetime",
            "subject",
            "classroom",
        ]


class BasicAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = [
            "id",
            "title",
            "is_active",
            "release_datetime",
            "due_datetime",
            "subject",
            "classroom",
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

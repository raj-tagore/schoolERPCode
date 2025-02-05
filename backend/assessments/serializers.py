from rest_framework import serializers

from .models import Assessment, StudentAssessment

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ["title", "description", "is_active", "syllabus", "datetime", "venue", "max_marks", "passing_marks", "submittted"]


class BasicAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ["id", "title", "datetime"]

class StudentAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAssessment
        fields = "__all__"



# serializers.py

from accounts.serializers import BasicTeacherSerializer
from rest_framework import serializers
from .models import Classroom, Subject
from accounts.models import Student, Teacher


class ClassroomSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Student.objects.all(), required=False
    )
    class_teacher = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(), required=False
    )
    class_teacher_details = BasicTeacherSerializer(
        source="class_teacher", read_only=True
    )
    other_teachers = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Teacher.objects.all(), required=False
    )

    class Meta:
        model = Classroom
        fields = [
            "id",
            "name",
            "is_active",
            "standard",
            "students",
            "class_teacher",
            "class_teacher_details",
            "other_teachers",
            "join_code",
        ]


class SubjectSerializer(serializers.ModelSerializer):
    classroom = serializers.PrimaryKeyRelatedField(
        queryset=Classroom.objects.all(), required=False
    )
    classroom_details = ClassroomSerializer(source="classroom", read_only=True)
    teacher = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(), required=False
    )
    teacher_details = BasicTeacherSerializer(source="teacher", read_only=True)

    class Meta:
        model = Subject
        fields = [
            "id",
            "name",
            "is_active",
            "description",
            "classroom",
            "classroom_details",
            "teacher",
            "teacher_details",
        ]

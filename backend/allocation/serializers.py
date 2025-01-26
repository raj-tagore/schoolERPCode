# serializers.py

import uuid
from rest_framework import serializers
from .models import Classroom, Subject
from accounts.models import Student, Teacher
from accounts.serializers import TeacherSerializer

class ClassroomSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(many=True,queryset=Student.objects.all(),required=False)
    class_teacher = TeacherSerializer(required=False)
    other_teachers = serializers.PrimaryKeyRelatedField(many=True,queryset=Teacher.objects.all(),required=False)

    class Meta:
        model = Classroom
        fields = [
            "id",
            "name",
            "is_active",
            "standard",
            "students",
            "class_teacher",
            "other_teachers",
            "join_code",
        ]

    def create(self, validated_data):
        students = validated_data.pop("students", [])
        other_teachers = validated_data.pop("other_teachers", [])
        classroom = Classroom.objects.create(**validated_data)
        classroom.students.set(students)
        classroom.other_teachers.set(other_teachers)
        return classroom

    def update(self, instance, validated_data):
        students = validated_data.pop("students", None)
        other_teachers = validated_data.pop("other_teachers", None)
        join_code = validated_data.pop("join_code", None)
        if join_code is not None:
            instance.join_code = join_code
        else:
            instance.join_code = uuid.uuid4()
        instance = super().update(instance, validated_data)
        if students is not None:
            instance.students.set(students)
        if other_teachers is not None:
            instance.other_teachers.set(other_teachers)

        return instance


class SubjectSerializer(serializers.ModelSerializer):
    classroom = ClassroomSerializer(required=False)
    teacher = TeacherSerializer(required=False)

    class Meta:
        model = Subject
        fields = [
            "id",
            "name",
            "is_active",
            "description",
            "classroom",
            "teacher",
        ]

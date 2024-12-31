from rest_framework import serializers
from accounts.models.student import Student
from allocation.models.classroom import Classroom
from allocation.models.qualification import Qualification


class BasicClassroomSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), required=True
    )

    classroom = serializers.PrimaryKeyRelatedField(
        queryset=Classroom.objects.all(), required=True
    )

    class Meta:
        model = Classroom
        fields = ["id", "student", "classroom", "marks", "grade", "remarks"]


class ClassroomSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), required=True
    )

    classroom = serializers.PrimaryKeyRelatedField(
        queryset=Classroom.objects.all(), required=True
    )

    class Meta:
        model = Classroom
        fields = ["id", "student", "classroom", "marks", "grade", "remarks", "file"]

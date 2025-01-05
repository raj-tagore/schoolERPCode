# serializers.py

from rest_framework import serializers
from .models import Classroom, Subject
from users.models import User


class ClassroomSerializer(serializers.ModelSerializer):
    # Fields for write operations
    students = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.filter(groups__name="Student"),
        required=False,
    )
    class_teacher = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(groups__name="Teacher"), required=False
    )
    other_teachers = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.filter(groups__name="Teacher"),
        required=False,
    )

    # Fields for read operations
    # students_details = UserSerializer(source="students", many=True, read_only=True)
    # class_teacher_details = UserSerializer(source="class_teacher", read_only=True)
    # other_teachers_details = UserSerializer(
    #     source="other_teachers", many=True, read_only=True
    # )

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
        instance = super().update(instance, validated_data)
        if students is not None:
            instance.students.set(students)
        if other_teachers is not None:
            instance.other_teachers.set(other_teachers)
        return instance


class SubjectSerializer(serializers.ModelSerializer):
    classroom = serializers.PrimaryKeyRelatedField(
        queryset=Classroom.objects.all(), required=False
    )
    main_teacher = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(groups__name="Teacher"), required=False
    )
    other_teachers = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.filter(groups__name="Teacher"),
        required=False,
    )
    additional_students = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.filter(groups__name="Student"),
        required=False,
    )

    # Fields for read operations
    # classroom_details = ClassroomSerializer(source="classroom", read_only=True)
    # main_teacher_details = UserSerializer(source="main_teacher", read_only=True)
    # other_teachers_details = UserSerializer(
    #     source="other_teachers", many=True, read_only=True
    # )
    # additional_students_details = UserSerializer(
    #     source="additional_students", many=True, read_only=True
    # )

    class Meta:
        model = Subject
        fields = [
            "id",
            "name",
            "is_active",
            "description",
            "classroom",
            "main_teacher",
            "other_teachers",
            "additional_students",
        ]

    def create(self, validated_data):
        other_teachers = validated_data.pop("other_teachers", [])
        additional_students = validated_data.pop("additional_students", [])
        subject = Subject.objects.create(**validated_data)
        subject.other_teachers.set(other_teachers)
        subject.additional_students.set(additional_students)
        return subject

    def update(self, instance, validated_data):
        other_teachers = validated_data.pop("other_teachers", None)
        additional_students = validated_data.pop("additional_students", None)
        instance = super().update(instance, validated_data)
        if other_teachers is not None:
            instance.other_teachers.set(other_teachers)
        if additional_students is not None:
            instance.additional_students.set(additional_students)
        return instance


class ClassroomJoinLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = [
            "id",
            "created_by",
            "created_on",
            "classroom",
            "uuid",
        ]

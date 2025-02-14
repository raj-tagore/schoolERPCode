from rest_framework import status
from rest_framework.response import Response
from .models import Classroom, Subject
from .serializers import ClassroomSerializer, SubjectSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    UpdateAPIView,
)
from .permissions import ClassroomPermissions, SubjectPermissions

from schoolERPCode.viewsets import get_standard_model_viewset


def classroom_filter(self, queryset, **kwargs):
    if "id" in kwargs:
        queryset = queryset.filter(id=kwargs["id"])
    if "name" in kwargs:
        queryset = queryset.filter(name__icontains=kwargs["name"])
    if "standard" in kwargs:
        queryset = queryset.filter(standards__id=kwargs["standard"])
    if "class_teacher" in kwargs:
        queryset = queryset.filter(class_teacher__id=kwargs["class_teacher"])
    if "student" in kwargs:
        queryset = queryset.filter(students__id=kwargs["student"])
    if "teacher" in kwargs:
        queryset = queryset.filter(other_teachers__id=kwargs["teacher"])

    return queryset


classroom_viewset = get_standard_model_viewset(
    queryset=Classroom.objects.all(),
    serializer_class=ClassroomSerializer,
    basic_serializer_class=ClassroomSerializer,
    filter_queryset=classroom_filter,
    permission_class=ClassroomPermissions,
)


class JoinClassroomView(UpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "join_code"

    def partial_update(self, request, *args, **kwargs):
        classroom = self.get_object()

        student = getattr(request.user, "student_account", None)
        if student is None:
            return Response(
                {"message": "You are not a student"}, status=status.HTTP_400_BAD_REQUEST
            )
        if student in classroom.students.all():
            return Response(
                {"message": "You are already in"}, status=status.HTTP_400_BAD_REQUEST
            )
        classroom.students.add(student)
        classroom.save()
        return Response(
            {"message": "Successfully joined the classroom"}, status=status.HTTP_200_OK
        )


def subject_filter(self, queryset, **kwargs):
    if "id" in kwargs:
        queryset = queryset.filter(id=kwargs["id"])
    if "name" in kwargs:
        queryset = queryset.filter(name__icontains=kwargs["name"])
    if "is_active" in kwargs:
        queryset = queryset.filter(is_active=kwargs["is_active"])
    if "description" in kwargs:
        queryset = queryset.filter(description__icontains=kwargs["description"])
    if "classroom" in kwargs:
        queryset = queryset.filter(classroom__id=kwargs["classroom"])
    if "main_teacher" in kwargs:
        queryset = queryset.filter(main_teacher__id=kwargs["main_teacher"])

    return queryset


subject_viewset = get_standard_model_viewset(
    queryset=Subject.objects.all(),
    serializer_class=SubjectSerializer,
    basic_serializer_class=SubjectSerializer,
    filter_queryset=subject_filter,
    permission_class=SubjectPermissions,
)

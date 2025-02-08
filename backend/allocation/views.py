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


def classroom_filter(
    self, queryset, id, name, standard, class_teacher, student, teacher
):
    if id:
        queryset = queryset.filter(id=id)
    if name:
        queryset = queryset.filter(name__icontains=name)
    if standard:
        queryset = queryset.filter(standards__id=standard)
    if class_teacher:
        queryset = queryset.filter(class_teacher__id=class_teacher)
    if student:
        queryset = queryset.filter(students__id=student)
    if teacher:
        queryset = queryset.filter(other_teachers__id=teacher)

    return queryset


classroom_viewset = get_standard_model_viewset(
    queryset=Classroom.objects.all(),
    serializer_class=ClassroomSerializer,
    basic_serializer_class=ClassroomSerializer,
    filter_queryset=classroom_filter,
    permission=ClassroomPermissions,
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


def subject_filter(
    self, queryset, id, name, is_active, description, classroom, main_teacher
):
    if id:
        queryset = queryset.filter(id=id)
    if name:
        queryset = queryset.filter(name__icontains=name)
    if is_active:
        queryset = queryset.filter(is_active=is_active)
    if description:
        queryset = queryset.filter(description__icontains=description)
    if classroom:
        queryset = queryset.filter(classroom__id=classroom)
    if main_teacher:
        queryset = queryset.filter(main_teacher__id=main_teacher)

    return queryset


subject_viewset = get_standard_model_viewset(
    queryset=Subject.objects.all(),
    serializer_class=SubjectSerializer,
    basic_serializer_class=SubjectSerializer,
    filter_queryset=subject_filter,
    permission=SubjectPermissions,
)

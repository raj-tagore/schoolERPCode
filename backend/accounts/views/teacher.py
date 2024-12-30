# accounts/views.py
from typing import final, override
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
    ListAPIView,
    CreateAPIView,
)

from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from accounts.models.teacher import Teacher
from accounts.permissions.teacher import TeacherPermissions
from accounts.serializers.teacher import TeacherReadSerializer, TeacherSerializer


@final
class AllTeachers(ListAPIView[Teacher]):
    queryset = Teacher.objects.all()
    serializer_class = TeacherReadSerializer
    permission_classes = [IsAuthenticated]

    @override
    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        id = request.query_params.get("id")
        fname = request.query_params.get("fname")
        lname = request.query_params.get("lname")
        group = request.query_params.get("group")


        if id:
            queryset = queryset.filter(id=id)
        if fname:
            queryset = queryset.filter(fname__icontains=fname)
        if lname:
            queryset = queryset.filter(lname__icontains=lname)
        if group:
            queryset = queryset.filter(groups__id=group)

        return queryset


@final
class AnyTeacher(RetrieveUpdateDestroyAPIView[Teacher]):
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated, TeacherPermissions]
    queryset = Teacher.objects.all()
    lookup_field = "id"


@final
class ReadTeacher(RetrieveAPIView[Teacher]):
    serializer_class = TeacherReadSerializer
    permission_classes = [IsAuthenticated]
    queryset = Teacher.objects.all()
    lookup_field = "id"

@final
class CreateTeacher(CreateAPIView[Teacher]):
    serializer_class = TeacherSerializer
    permission_classes = [DjangoModelPermissions]

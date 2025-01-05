from django.shortcuts import render

from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
    CreateAPIView
)
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from .models import Parent, Teacher, Student
from .serializers import (
    ParentSerializer,
    TeacherSerializer,
    StudentSerializer,
)

class AllParents(ListAPIView):
    serializer_class = ParentSerializer
    permission_classes = [IsAuthenticated]
    queryset = Parent.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        # filter parents of student here
        return queryset

class AnyParent(RetrieveUpdateDestroyAPIView):
    serializer_class = ParentSerializer
    permission_classes = [IsAuthenticated]
    queryset = Parent.objects.all()
    lookup_field = 'id'  # or 'pk' if you prefer

class CreateParent(CreateAPIView):
    serializer_class = ParentSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = Parent.objects.all()


class AllTeachers(ListAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]
    queryset = Teacher.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        # filter parents of student here
        return queryset

class AnyTeacher(RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]
    queryset = Teacher.objects.all()
    lookup_field = 'id'

class CreateTeacher(CreateAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = Teacher.objects.all()
    

class AllStudents(ListAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        # filter parents of student here
        return queryset

class AnyStudent(RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    lookup_field = 'id'

class CreateStudent(CreateAPIView):
    serializer_class = StudentSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = Student.objects.all()
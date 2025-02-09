from django.shortcuts import render
from django.db.models import Q

from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
    CreateAPIView
)
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count

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

        name = request.query_params.get('name')
        if name: 
            queryset = queryset.filter(
                Q(user__first_name__icontains=name) | Q(user__last_name__icontains=name)
            )

        return queryset

class AnyParent(RetrieveUpdateDestroyAPIView):
    serializer_class = ParentSerializer
    permission_classes = [IsAuthenticated]
    queryset = Parent.objects.all()
    lookup_field = 'id' 

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
        id = request.query_params.get('id')
        classrooms_leading = request.query_params.get('classrooms_leading')
        classrooms_assisting = request.query_params.get('classrooms_assisting')
        classrooms = request.query_params.get('classrooms')
        name = request.query_params.get('name')

        if id:
            queryset = queryset.filter(id=id)
        if classrooms_leading:
            queryset = queryset.filter(classrooms_leading__id=classrooms_leading)
        if classrooms_assisting:
            queryset = queryset.filter(classrooms_assisting__id=classrooms_assisting)
        if classrooms:
            queryset = queryset.filter(
                Q(classrooms_leading__id=classrooms) | Q(classrooms_assisting__id=classrooms)
            ).distinct()
        if name: 
            queryset = queryset.filter(
                Q(user__first_name__icontains=name) | Q(user__last_name__icontains=name)
            )

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

        id = request.query_params.get('id')
        classrooms = request.query_params.get('classroom')
        name = request.query_params.get('name')

        if id:
            queryset = queryset.filter(id=id)
        if classrooms:
            queryset = queryset.filter(classrooms__id=classrooms)
        if name: 
            queryset = queryset.filter(
                Q(user__first_name__icontains=name) | Q(user__last_name__icontains=name)
            )

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

class StudentStats(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        stats = {
            'total': Student.objects.count(),
            'pending_approval': Student.objects.filter(user__is_approved=False).count(),
        }
        return Response(stats)

class ParentStats(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        stats = {
            'total': Parent.objects.count(),
            'pending_approval': Parent.objects.filter(user__is_approved=False).count(),
        }
        return Response(stats)

class TeacherStats(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        stats = {
            'total': Teacher.objects.count(),
            'pending_approval': Teacher.objects.filter(user__is_approved=False).count(),
        }
        return Response(stats)
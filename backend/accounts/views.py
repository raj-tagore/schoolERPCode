from django.db.models import Q

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Parent, Teacher, Student
from .serializers import (
    BasicTeacherSerializer,
    ParentSerializer,
    TeacherSerializer,
    StudentSerializer,
)

from schoolERPCode.viewsets import get_standard_model_viewset

def parent_filter(self, queryset, name):
    if name:
        queryset = queryset.filter(
            Q(user__first_name__icontains=name) | Q(user__last_name__icontains=name)
        )
    return queryset

parent_viewset = get_standard_model_viewset(
    queryset=Parent.objects.all(),
    serializer_class=ParentSerializer,
    basic_serializer_class=ParentSerializer,
    filter_queryset=parent_filter,
)

def teacher_filter(
    self, queryset, classrooms_leading, classrooms_assisting, classrooms, name
):
    if id:
        queryset = queryset.filter(id=id)
    if classrooms_leading:
        queryset = queryset.filter(classrooms_leading__id=classrooms_leading)
    if classrooms_assisting:
        queryset = queryset.filter(classrooms_assisting__id=classrooms_assisting)
    if classrooms:
        queryset = queryset.filter(
            Q(classrooms_leading__id=classrooms)
            | Q(classrooms_assisting__id=classrooms)
        ).distinct()
    if name:
        queryset = queryset.filter(
            Q(user__first_name__icontains=name) | Q(user__last_name__icontains=name)
        )
    return queryset


teacher_viewset = get_standard_model_viewset(
    queryset=Teacher.objects.all(),
    serializer_class=TeacherSerializer,
    basic_serializer_class=BasicTeacherSerializer,
    filter_queryset=teacher_filter,
)

def student_filter(self, queryset, classrooms, name):
    if id:
        queryset = queryset.filter(id=id)
    if classrooms:
        queryset = queryset.filter(classrooms__id=classrooms)
    if name:
        queryset = queryset.filter(
            Q(user__first_name__icontains=name) | Q(user__last_name__icontains=name)
        )
    return queryset

student_viewset = get_standard_model_viewset(
    queryset = Student.objects.all(),
    serializer_class = StudentSerializer,
    basic_serializer_class=StudentSerializer,
    filter_queryset=student_filter,
)

class StudentStats(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        stats = {
            "total": Student.objects.count(),
            "pending_approval": Student.objects.filter(user__is_approved=False).count(),
        }
        return Response(stats)


class ParentStats(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        stats = {
            "total": Parent.objects.count(),
            "pending_approval": Parent.objects.filter(user__is_approved=False).count(),
        }
        return Response(stats)


class TeacherStats(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        stats = {
            "total": Teacher.objects.count(),
            "pending_approval": Teacher.objects.filter(user__is_approved=False).count(),
        }
        return Response(stats)

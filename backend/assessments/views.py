from django.shortcuts import render

from assessments.models import Assessment, StudentAssessment
from assessments.permissions import AssessmentPermissions
from assessments.serializers import AssessmentSerializer, StudentAssessmentSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView

# Create your views here.
class AllAssessments(ListAPIView):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request



        title = request.query_params.get('title')
        description = request.query_params.get('description')
        is_active = request.query_params.get('is_active')
        syllabus = request.query_params.get('syllabus')
        start = request.query_params.get('start')
        end = request.query_params.get('end')
        venue = request.query_params.get('venue')
        subject = request.query_params.get('subject')
        max_marks = request.query_params.get('max_marks')
        passing_marks = request.query_params.get('passing_marks')

        if start:
            queryset = queryset.filter(start=start)
        if end:
            queryset = queryset.filter(end=end)
        if day:
            queryset = queryset.filter(day=day)

        return queryset

class AnyAssessment(RetrieveUpdateDestroyAPIView):
    serializer_class = AssessmentSerializer
    permission_classes = [IsAuthenticated, AssessmentPermissions]
    queryset = Assessment.objects.all()
    lookup_field = 'id'

class CreateAssessment(CreateAPIView):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    permission_classes = [DjangoModelPermissions]

# Create your views here.
class AllStudentAssessments(ListAPIView):
    queryset = StudentAssessment.objects.all()
    serializer_class = StudentAssessmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        id = request.query_params.get('id')
        start = request.query_params.get('start')
        end = request.query_params.get('end')
        day = request.query_params.get('day')

        if id:
            queryset = queryset.filter(id=id)
        if start:
            queryset = queryset.filter(start=start)
        if end:
            queryset = queryset.filter(end=end)
        if day:
            queryset = queryset.filter(day=day)

        return queryset

class AnyStudentAssessment(RetrieveUpdateDestroyAPIView):
    serializer_class = StudentAssessmentSerializer
    permission_classes = [IsAuthenticated, AssessmentPermissions]
    queryset = StudentAssessment.objects.all()
    lookup_field = 'id'

class CreateStudentAssessment(CreateAPIView):
    queryset = StudentAssessment.objects.all()
    serializer_class = StudentAssessmentSerializer
    permission_classes = [DjangoModelPermissions]

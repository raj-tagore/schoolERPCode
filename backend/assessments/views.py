from assessments.models import Assessment, StudentAssessment
from assessments.permissions import AssessmentPermissions
from assessments.serializers import AssessmentSerializer, StudentAssessmentSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    CreateAPIView,
)

from schoolERPCode.viewsets import get_standard_model_viewset


def assessment_filter(
    self,
    queryset,
    title,
    description,
    is_active,
    syllabus,
    start,
    end,
    venue,
    subject,
    max_marks,
    passing_marks,
):
    if title:
        queryset = queryset.filter(title__icontains=title)
    if start:
        queryset = queryset.filter(datetime__gte=start)
    if end:
        queryset = queryset.filter(datetime__lte=end)
    if description:
        queryset = queryset.filter(description__icontains=description)
    if is_active:
        queryset = queryset.filter(is_active=is_active)
    if syllabus:
        queryset = queryset.filter(syllabus__icontains=syllabus)
    if venue:
        queryset = queryset.filter(venue__icontains=venue)
    if subject:
        queryset = queryset.filter(subject__id=subject)
    if max_marks:
        queryset = queryset.filter(max_marks=max_marks)
    if passing_marks:
        queryset = queryset.filter(passing_marks=passing_marks)

    return queryset


assessment_viewset = get_standard_model_viewset(
    queryset=Assessment.objects.all(),
    serializer_class=AssessmentSerializer,
    filter_queryset=assessment_filter,
    basic_serializer_class=AssessmentSerializer,
)


def student_assessment_filter(self, queryset, student, assessment, marks, status):
    if student:
        queryset = queryset.filter(student__id=student)
    if assessment:
        queryset = queryset.filter(assessment__id=assessment)
    if marks:
        queryset = queryset.filter(marks=marks)
    if status:
        queryset = queryset.filter(status=status)

    return

student_assessment_viewset = get_standard_model_viewset(
    queryset=StudentAssessment.objects.all(),
    serializer_class=StudentAssessmentSerializer,
    filter_queryset=student_assessment_filter,
    basic_serializer_class=StudentAssessmentSerializer,
)

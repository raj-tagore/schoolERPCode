from assessments.models import Assessment, StudentAssessment
from assessments.permissions import AssessmentPermissions
from assessments.serializers import AssessmentSerializer, StudentAssessmentSerializer
from schoolERPCode.viewsets import get_standard_model_viewset


def assessment_filter(
    self,
    queryset,
    **kwargs
):
    if  "title"  in kwargs:
        queryset = queryset.filter(title__icontains=kwargs[ "title" ])
    if  "start"  in kwargs:
        queryset = queryset.filter(datetime__gte=kwargs[ "start" ])
    if  "end"  in kwargs:
        queryset = queryset.filter(datetime__lte=kwargs[ "end" ])
    if  "description"  in kwargs:
        queryset = queryset.filter(description__icontains=kwargs[ "description" ])
    if  "is_active"  in kwargs:
        queryset = queryset.filter(is_active=kwargs[ "is_active" ])
    if  "syllabus"  in kwargs:
        queryset = queryset.filter(syllabus__icontains=kwargs[ "syllabus" ])
    if  "venue"  in kwargs:
        queryset = queryset.filter(venue__icontains=kwargs[ "venue" ])
    if  "subject"  in kwargs:
        queryset = queryset.filter(subject__id=kwargs[ "subject" ])
    if  "max_marks"  in kwargs:
        queryset = queryset.filter(max_marks=kwargs[ "max_marks" ])
    if  "passing_marks"  in kwargs:
        queryset = queryset.filter(passing_marks=kwargs[ "passing_marks" ])

    return queryset


assessment_viewset = get_standard_model_viewset(
    queryset=Assessment.objects.all(),
    serializer_class=AssessmentSerializer,
    filter_queryset=assessment_filter,
    basic_serializer_class=AssessmentSerializer,
    permission_class=AssessmentPermissions,
)


def student_assessment_filter(self, queryset, **kwargs):
    if "student" in kwargs:
        queryset = queryset.filter(student__id=kwargs["student"])
    if "assessment" in kwargs:
        queryset = queryset.filter(assessment__id=kwargs["assessment"])
    if "marks" in kwargs:
        queryset = queryset.filter(marks=kwargs["marks"])
    if "status" in kwargs:
        queryset = queryset.filter(status=kwargs["status"])

    return

student_assessment_viewset = get_standard_model_viewset(
    queryset=StudentAssessment.objects.all(),
    serializer_class=StudentAssessmentSerializer,
    filter_queryset=student_assessment_filter,
    basic_serializer_class=StudentAssessmentSerializer,
    permission_class=AssessmentPermissions,
)

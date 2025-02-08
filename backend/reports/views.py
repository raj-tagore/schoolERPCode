from .models import AttendanceReport
from .serializers import AttendanceReportSerializer
from schoolERPCode.viewsets import get_standard_model_viewset


def attendance_report_filter(self, queryset, **kwargs):
    if "submitted_by" in kwargs:
        queryset = queryset.filter(metadata__submitted_by=kwargs["submitted_by"])
    if "submitted_start" in kwargs:
        queryset = queryset.filter(metadata__submitted_at__gte=kwargs["submitted_start"])
    if "submitted_end" in kwargs:
        queryset = queryset.filter(metadata__submitted_at__lte=kwargs["submitted_end"])
    if "attachment" in kwargs:
        queryset = queryset.filter(metadata__attachment=kwargs["attachment"])
    if "is_approved" in kwargs:
        queryset = queryset.filter(metadata__is_approved=kwargs["is_approved"])
    if "approved_by" in kwargs:
        queryset = queryset.filter(metadata__approved_by=kwargs["approved_by"])
    if "approved_start" in kwargs:
        queryset = queryset.filter(metadata__approved_at__gte=kwargs["approved_start"])
    if "approved_end" in kwargs:
        queryset = queryset.filter(metadata__approved_at__lte=kwargs["approved_end"])
    if "attendance_date_start" in kwargs:
        queryset = queryset.filter(date__gte=kwargs["attendance_date_start"])
    if "attendance_date_end" in kwargs:
        queryset = queryset.filter(date__lte=kwargs["attendance_date_end"])
    if "classroom" in kwargs:
        queryset = queryset.filter(classroom=kwargs["classroom"])
    if "remarks" in kwargs:
        queryset = queryset.filter(remarks__icontains=kwargs["remarks"])

    return queryset


attendance_report_views = get_standard_model_viewset(
    queryset=AttendanceReport.objects.all(),
    serializer_class=AttendanceReportSerializer,
    basic_serializer_class=AttendanceReportSerializer,
    filter_queryset=attendance_report_filter,
)

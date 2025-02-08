from .models import AttendanceReport
from .serializers import AttendanceReportSerializer
from schoolERPCode.viewsets import get_standard_model_viewset


def attendance_report_filter(
    self,
    queryset,
    submitted_by,
    submitted_start,
    submitted_end,
    attachment,
    is_approved,
    approved_by,
    approved_start,
    approved_end,
    attendance_date_start,
    attendance_date_end,
    classroom,
    remarks,
):
    if submitted_by:
        queryset = queryset.filter(metadata__submitted_by=submitted_by)
    if submitted_start:
        queryset = queryset.filter(metadata__submitted_at__gte=submitted_start)
    if submitted_end:
        queryset = queryset.filter(metadata__submitted_at__lte=submitted_end)
    if attachment:
        queryset = queryset.filter(metadata__attachment=attachment)
    if is_approved:
        queryset = queryset.filter(metadata__is_approved=is_approved)
    if approved_by:
        queryset = queryset.filter(metadata__approved_by=approved_by)
    if approved_start:
        queryset = queryset.filter(metadata__approved_at__gte=approved_start)
    if approved_end:
        queryset = queryset.filter(metadata__approved_at__lte=approved_end)
    if attendance_date_start:
        queryset = queryset.filter(date__gte=attendance_date_start)
    if attendance_date_end:
        queryset = queryset.filter(date__lte=attendance_date_end)
    if classroom:
        queryset = queryset.filter(classroom=classroom)
    if remarks:
        queryset = queryset.filter(remarks__icontains=remarks)

    return queryset

attendance_report_views = get_standard_model_viewset(
    queryset=AttendanceReport.objects.all(),
    serializer_class=AttendanceReportSerializer,
    basic_serializer_class=AttendanceReportSerializer,
    filter_queryset=attendance_report_filter,
)


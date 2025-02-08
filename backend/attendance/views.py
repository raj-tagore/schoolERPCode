from attendance.models import Attendance
from attendance.serializers import AttendanceSerializer

from schoolERPCode.viewsets import get_standard_model_viewset


def attendance_filter(self, queryset, date, start, end, absentees, subject, classroom):
    if date:
        queryset = queryset.filter(date=date)
    if start:
        queryset = queryset.filter(date__gte=start)
    if end:
        queryset = queryset.filter(date__lte=end)
    if absentees:
        queryset = queryset.filter(absentees__id__in=absentees)
    if subject:
        queryset = queryset.filter(subject__id=subject)
    if classroom:
        queryset = queryset.filter(classroom__id=classroom)

    return queryset


attendance_viewset = get_standard_model_viewset(
    queryset=Attendance.objects.all(),
    serializer_class=AttendanceSerializer,
    basic_serializer_class=AttendanceSerializer,
    filter_queryset=attendance_filter,
)



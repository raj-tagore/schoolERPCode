from attendance.models import Attendance
from attendance.serializers import AttendanceSerializer

from schoolERPCode.viewsets import get_standard_model_viewset


def attendance_filter(self, queryset, **kwargs):
    if "date" in kwargs:
        queryset = queryset.filter(date=kwargs["date"])
    if "start" in kwargs:
        queryset = queryset.filter(date__gte=kwargs["start"])
    if "end" in kwargs:
        queryset = queryset.filter(date__lte=kwargs["end"])
    if "absentees" in kwargs:
        queryset = queryset.filter(absentees__id__in=kwargs["absentees"])
    if "subject" in kwargs:
        queryset = queryset.filter(subject__id=kwargs["subject"])
    if "classroom" in kwargs:
        queryset = queryset.filter(classroom__id=kwargs["classroom"])

    return queryset


attendance_viewset = get_standard_model_viewset(
    queryset=Attendance.objects.all(),
    serializer_class=AttendanceSerializer,
    basic_serializer_class=AttendanceSerializer,
    filter_queryset=attendance_filter,
)

from timetable.models import Period, TimeTable
from timetable.permissions import PeriodPermissions, TimeTablePermissions
from timetable.serializers import PeriodSerializer, TimeTableSerializer

from schoolERPCode.viewsets import get_standard_model_viewset


def periods_filter(self, queryset, id, start, end, day):
    if id:
        queryset = queryset.filter(id=id)
    if start:
        queryset = queryset.filter(start=start)
    if end:
        queryset = queryset.filter(end=end)
    if day:
        queryset = queryset.filter(day=day)

    return queryset

periods_viewset = get_standard_model_viewset(
    queryset=Period.objects.all(),
    serializer_class=PeriodSerializer,
    basic_serializer_class=PeriodSerializer,
    filter_queryset=periods_filter,
    permission_class=PeriodPermissions,
)

def timetable_filter(self, queryset, id, subject, periods):
    if id:
        queryset = queryset.filter(id=id)
    if subject:
        queryset = queryset.filter(subject__id=subject)
    if periods:
        queryset = queryset.filter(periods__id=subject)

    return queryset

timetable_viewset = get_standard_model_viewset(
    queryset=TimeTable.objects.all(),
    serializer_class=TimeTableSerializer,
    basic_serializer_class=TimeTableSerializer,
    permission_class=TimeTablePermissions,
    filter_queryset=timetable_filter,
)

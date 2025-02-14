from timetable.models import Period, TimeTable
from timetable.permissions import PeriodPermissions, TimeTablePermissions
from timetable.serializers import PeriodSerializer, TimeTableSerializer

from schoolERPCode.viewsets import get_standard_model_viewset


def periods_filter(self, queryset, **kwargs):
    if "id" in kwargs:
        queryset = queryset.filter(id=kwargs["id"])
    if "start" in kwargs:
        queryset = queryset.filter(start=kwargs["start"])
    if "end" in kwargs:
        queryset = queryset.filter(end=kwargs["end"])
    if "day" in kwargs:
        queryset = queryset.filter(day=kwargs["day"])

    return queryset


periods_viewset = get_standard_model_viewset(
    queryset=Period.objects.all(),
    serializer_class=PeriodSerializer,
    basic_serializer_class=PeriodSerializer,
    filter_queryset=periods_filter,
    permission_class=PeriodPermissions,
)


def timetable_filter(self, queryset, **kwargs):
    if "id" in kwargs:
        queryset = queryset.filter(id=kwargs["id"])
    if "subject" in kwargs:
        queryset = queryset.filter(subject__id=kwargs["subject"])
    if "periods" in kwargs:
        queryset = queryset.filter(periods__id=kwargs["subject"])

    return queryset


timetable_viewset = get_standard_model_viewset(
    queryset=TimeTable.objects.all(),
    serializer_class=TimeTableSerializer,
    basic_serializer_class=TimeTableSerializer,
    permission_class=TimeTablePermissions,
    filter_queryset=timetable_filter,
)

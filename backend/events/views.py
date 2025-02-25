from events.models import Event
from events.permissions import EventPermissions
from events.serializers import EventSerializer, EventBaseSerializer
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    CreateAPIView,
)
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response
from schoolERPCode.viewsets import get_standard_model_viewset


def events_filter(self, queryset, **kwargs):
    if "id" in kwargs:
        queryset = queryset.filter(id=kwargs["id"])
    if "title" in kwargs:
        queryset = queryset.filter(title__icontains=kwargs["title"])
    if "description" in kwargs: 
        queryset = queryset.filter(description__icontains=kwargs["description"])
    if "is_school_wide" in kwargs:
        queryset = queryset.filter(is_school_wide=kwargs["is_school_wide"])
    if "classrooms" in kwargs:
        queryset = queryset.filter(classrooms__id__in=kwargs["classrooms"])
    if "subjects" in kwargs:
        queryset = queryset.filter(subjects__id__in=kwargs["subjects"])
    if "month" in kwargs and "year" in kwargs:
        month = int(kwargs["month"])
        year = int(kwargs["year"])
        queryset = queryset.filter(start__year=year, start__month=month)
    if "start_date" in kwargs:
        queryset = queryset.filter(start__gte=kwargs["start_date"])
    if "end_date" in kwargs:
        queryset = queryset.filter(start__lte=kwargs["end_date"])

    return queryset


events_viewset = get_standard_model_viewset(
    queryset=Event.objects.all(),
    serializer_class=EventSerializer,
    basic_serializer_class=EventSerializer,
    permission_class=EventPermissions,
    filter_queryset=events_filter,
)

class Calendar(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        queryset = super().get_queryset()
        return events_filter(self, queryset, **self.request.query_params.dict())

    



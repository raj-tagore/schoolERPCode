from events.models import Event
from events.permissions import EventPermissions
from events.serializers import EventSerializer
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

    return queryset


events_viewset = get_standard_model_viewset(
    queryset=Event.objects.all(),
    serializer_class=EventSerializer,
    basic_serializer_class=EventSerializer,
    permission_class=EventPermissions,
    filter_queryset=events_filter,
)

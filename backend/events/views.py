from assessments.models import Assessment
from assessments.serializers import BasicAssessmentSerializer
from events.models import Calendar, Event
from events.permissions import EventPermissions
from events.serializers import CalendarSerializer, EventSerializer
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    CreateAPIView,
)
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from rest_framework.response import Response

from schoolERPCode.viewsets import get_standard_model_viewset


def calendars_filter(
    self, queryset, name, description, is_school_wide, classrooms, subjects, users
):
    if id:
        queryset = queryset.filter(id=id)
    if name:
        queryset = queryset.filter(name__icontains=name)
    if description:
        queryset = queryset.filter(description__icontains=description)
    if is_school_wide:
        queryset = queryset.filter(is_school_wide=is_school_wide)
    if classrooms:
        queryset = queryset.filter(classrooms__id__in=classrooms)
    if subjects:
        queryset = queryset.filter(subjects__id__in=subjects)
    if users:
        queryset = queryset.filter(users__id__in=users)

    return queryset


calendars_viewset = get_standard_model_viewset(
    queryset=Calendar.objects.all(),
    serializer_class=CalendarSerializer,
    basic_serializer_class=CalendarSerializer,
    permission_class=EventPermissions,
    filter_queryset=calendars_filter,
)



class AllEvents(ListAPIView):
    permission_classes = [IsAuthenticated]

    # Won't be handling pagination for this, so we need to be slightly more careful when retriving, in particular, we should always specify a start and end
    # Order shouldn't matter since we are going to be putting this based on the datetime or start
    def list(self, request):
        events_queryset = Event.objects.all()
        # for adding Assessment
        assessment_queryset = Assessment.objects.all()

        title = request.query_params.get("title")
        calendar = request.query_params.get("calendar")
        start = request.query_params.get("start")
        end = request.query_params.get("end")

        # Need to add filters for both models
        if title:
            events_queryset = events_queryset.filter(title__icontains=title)
            assessment_queryset = assessment_queryset.filter(title__icontains=title)
        if start:
            events_queryset = events_queryset.filter(start__gte=start)
            assessment_queryset = assessment_queryset.filter(datetime__gte=start)
        if end:
            events_queryset = events_queryset.filter(end__lte=end)
            assessment_queryset = assessment_queryset.filter(end__lte=end)
        if calendar:
            events_queryset = events_queryset.filter(calendar__id=calendar)
            calendar = Calendar.objects.get(id=calendar)
            assessment_queryset = assessment_queryset.filter(
                subject__in=calendar.subjects.all()
            )

        event_data = EventSerializer(events_queryset, many=True).data
        assessment_data = BasicAssessmentSerializer(assessment_queryset, many=True).data

        # Don't like this, need another way to do this
        for event in event_data:
            event["type"] = "event"
        for assessment in assessment_data:
            assessment["type"] = "exam"

        combined_data = event_data + assessment_data

        return Response(combined_data)


class AnyEvent(RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, EventPermissions]
    queryset = Event.objects.all()
    lookup_field = "id"


class CreateEvent(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [DjangoModelPermissions]

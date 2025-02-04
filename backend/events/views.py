from events.models import Event
from events.permissions import EventPermissions
from events.serializers import EventSerializer
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    CreateAPIView,
)
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions


class AllEvents(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        id = request.query_params.get("id")
        title = request.query_params.get("title")
        description = request.query_params.get("description")
        attachment = request.query_params.get("attachment")
        date = request.query_params.get("date")
        classroom = request.query_params.get("classroom")
        repeat_period = request.query_params.get("repeat_period")

        if id:
            queryset = queryset.filter(id=id)
        if title:
            queryset = queryset.filter(title__icontains=title)
        if description:
            queryset = queryset.filter(description__icontains=description)
        if attachment:
            queryset = queryset.filter(attachment=attachment)
        if date:
            queryset = queryset.filter(date=date)
        if classroom:
            queryset = queryset.filter(classroom=classroom)
        if repeat_period:
            queryset = queryset.filter(repeat_period=repeat_period)

        return queryset


class AnyEvent(RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, EventPermissions]
    queryset = Event.objects.all()
    lookup_field = "id"


class CreateEvent(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [DjangoModelPermissions]

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
        start = request.query_params.get("start")
        end = request.query_params.get("end")
        day = request.query_params.get("day")

        if id:
            queryset = queryset.filter(id=id)
        if start:
            queryset = queryset.filter(start=start)
        if end:
            queryset = queryset.filter(end=end)
        if day:
            queryset = queryset.filter(day=day)

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

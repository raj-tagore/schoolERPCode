from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView
from timetable.models import Period, TimeTable
from timetable.permissions import PeriodPermissions, TimeTablePermissions
from timetable.serializers import PeriodSerializer, TimeTableSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

# Create your views here.
class AllPeriods(ListAPIView):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        id = request.query_params.get('id')
        start = request.query_params.get('start')
        end = request.query_params.get('end')
        day = request.query_params.get('day')

        if id:
            queryset = queryset.filter(id=id)
        if start:
            queryset = queryset.filter(start=start)
        if end:
            queryset = queryset.filter(end=end)
        if day:
            queryset = queryset.filter(day=day)

        return queryset

class AnyPeriod(RetrieveUpdateDestroyAPIView):
    serializer_class = PeriodSerializer
    permission_classes = [IsAuthenticated, PeriodPermissions]
    queryset = Period.objects.all()
    lookup_field = 'id'

class CreatePeriod(CreateAPIView):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer
    permission_classes = [DjangoModelPermissions]


class AllTimeTables(ListAPIView):
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        id = request.query_params.get('id')
        subject = request.query_params.get('name')
        periods = request.query_params.get('periods')

        if id:
            queryset = queryset.filter(id=id)
        if subject:
            queryset = queryset.filter(subject__id=subject)
        if periods:
            queryset = queryset.filter(periods__id=subject)

        return queryset

class AnyTimeTable(RetrieveUpdateDestroyAPIView):
    serializer_class = TimeTableSerializer
    permission_classes = [IsAuthenticated, TimeTablePermissions]
    queryset = TimeTable.objects.all()
    lookup_field = 'id'

class CreateTimeTable(CreateAPIView):
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer
    permission_classes = [DjangoModelPermissions]


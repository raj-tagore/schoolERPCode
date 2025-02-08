from django.shortcuts import render

from attendance.models import Attendance
from attendance.serializers import AttendanceSerializer

from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    CreateAPIView,
)
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions



# Create your views here.
class AllAttendances(ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        date = request.query_params.get("date")
        start = request.query_params.get("start")
        end = request.query_params.get("end")
        absentees = request.query_params.get("absentees")
        subject = request.query_params.get("subject")
        classroom = request.query_params.get("classroom")

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


class AnyAttendance(RetrieveUpdateDestroyAPIView):
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Attendance.objects.all()
    lookup_field = "id"


class CreateAttendance(CreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [DjangoModelPermissions]

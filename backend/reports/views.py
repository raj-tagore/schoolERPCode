from django.shortcuts import render

from reports.models import Report, SubmittedReport
from reports.serializers import ReportSerializer, SubmittedReportSerializer

from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    CreateAPIView,
)
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions


# Create your views here.
class AllReports(ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        name = request.query_params.get("name")
        description = request.query_params.get("description")
        start = request.query_params.get("start")
        end = request.query_params.get("end")
        assigned_to = request.query_params.get("assigned_to")
        submission_deadline = request.query_params.get("submission_deadline")
        submission_frequency = request.query_params.get("submission_frequency")
        is_active = request.query_params.get("is_active")

        if id:
            queryset = queryset.filter(id=id)
        if name:
            queryset = queryset.filter(name__icontains=name)
        if description:
            queryset = queryset.filter(description__icontains=description)
        if start:
            queryset = queryset.filter(created_at__gte=start)
        if end:
            queryset = queryset.filter(created_at__lte=end)
        if assigned_to:
            queryset = queryset.filter(assigned_to=assigned_to)
        if submission_deadline:
            queryset = queryset.filter(submission_deadline__lte=submission_deadline)
        if submission_frequency:
            queryset = queryset.filter(submission_frequency__lte=submission_frequency)
        if is_active:
            queryset = queryset.filter(is_active__lte=is_active)

        return queryset


class AnyReport(RetrieveUpdateDestroyAPIView):
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Report.objects.all()
    lookup_field = "id"


class CreateReport(CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [DjangoModelPermissions]


# Create your views here.
class AllSubmittedReports(ListAPIView):
    queryset = SubmittedReport.objects.all()
    serializer_class = SubmittedReportSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        report = request.query_params.get("report")
        title = request.query_params.get("title")
        description = request.query_params.get("description")
        submitted_by = request.query_params.get("submitted_by")
        start = request.query_params.get("start")
        end = request.query_params.get("end")
        attachment = request.query_params.get("attachment")
        is_approved = request.query_params.get("is_approved")
        approved_by = request.query_params.get("approved_by")

        if report:
            queryset = queryset.filter(report__id=report)
        if title:
            queryset = queryset.filter(title__icontains=title)
        if description:
            queryset = queryset.filter(description__icontains=description)
        if submitted_by:
            queryset = queryset.filter(submitted_by__id=submitted_by)
        if start:
            queryset = queryset.filter(submitted_at__gte=start)
        if end:
            queryset = queryset.filter(submitted_at__lte=start)
        if attachment:
            queryset = queryset.filter(attachment__id=attachment)
        if is_approved:
            queryset = queryset.filter(is_approved__id=is_approved)
        if approved_by:
            queryset = queryset.filter(approved_by__id=approved_by)

        return queryset


class AnySubmittedReport(RetrieveUpdateDestroyAPIView):
    serializer_class = SubmittedReportSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = SubmittedReport.objects.all()
    lookup_field = "id"


class CreateSubmittedReport(CreateAPIView):
    queryset = SubmittedReport.objects.all()
    serializer_class = SubmittedReportSerializer
    permission_classes = [DjangoModelPermissions]

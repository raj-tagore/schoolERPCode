from reports.models import Report, SubmittedReport
from rest_framework import serializers

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"

class SubmittedReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmittedReport
        fields = "__all__"

from reports.models import ReportMeta, AttendanceReport
from rest_framework import serializers

class ReportMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportMeta
        fields = "__all__"

class AttendanceReportSerializer(serializers.ModelSerializer):
    metadata = ReportMetaSerializer(source="metadata")
    class Meta:
        model = AttendanceReport
        fields = "__all__"

    def create(self, validated_data):
        metadata_data = validated_data.pop('metadata')
        report = AttendanceReport.objects.create(**validated_data)
        ReportMeta.objects.create(attendance_report=report, **metadata_data)
        return report

    def update(self, instance, validated_data):
        # Provided from Gemini as is
        metadata_data = validated_data.pop('metadata')
        if metadata_data:  # Only update metadata if it's provided
            for attr, value in metadata_data.items():
                setattr(instance.metadata, attr, value) # More efficient and concise
            instance.metadata.save()

        for attr, value in validated_data.items():  # Iterate through validated data
            setattr(instance, attr, value) # More efficient and concise
        instance.save()

        return instance


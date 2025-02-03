from allocation.models import Subject
from rest_framework import serializers
from .models import TimeTable, Period


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ["__all__"]


class TimeTableSerializer(serializers.ModelSerializer):
    periods = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Period.objects.all(), required=False
    )
    periods_details = PeriodSerializer(source="periods", read_only=True)

    class Meta:
        model = TimeTable
        fields = "__all__"

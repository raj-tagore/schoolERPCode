from rest_framework import serializers
from .models import Purpose, Payee, Record
from accounts.serializers import StudentSerializer


class PurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purpose
        fields = "__all__"


class PayeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payee
        fields = "__all__"


class BasicPayeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payee
        fields = ["name", "email", "id"]


class RecordSerializer(serializers.ModelSerializer):
    purpose_details = PurposeSerializer(source="purpose")
    payee_details = BasicPayeeSerializer(source="payee")
    student_details = StudentSerializer(source="student")

    class Meta:
        model = Record
        fields = "__all__"


# accounts/serializers.py

from typing import final, override
from rest_framework import serializers

from accounts.models.student import Student


@final
class StudentSerializer(serializers.ModelSerializer[Student]):
    @override
    @final
    class Meta:
        model = Student
        fields = [
            "id",
            "account",
            "classroom",
            "guardian1",
            "guardian2",
            "address_proof",
            "birth_certificate",
            "identity_proof_type",
            "identity_proof_number",
            "identity_proof",
            "character_certificate",
            "id_card",
            "leaving_certificate",
        ]


class StudentReadSerializer(serializers.ModelSerializer[Student]):
    @final
    class Meta:
        model = Student
        fields = [
            "id",
            "account",
            "classroom",
        ]

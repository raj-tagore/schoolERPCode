# accounts/serializers.py

from rest_framework import serializers

from accounts.models.student import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "id",
            "account",
            "roll_no",
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
        extra_kwargs = {
            "password": {"write_only": True},
            "groups": {"required": False},
            "user_permissions": {"required": False},
        }


class AccountReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "whatsapp",
            "classrooms",
            "subjects",
        ]

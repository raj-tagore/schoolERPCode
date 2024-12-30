# accounts/serializers.py

from typing import final, override
from rest_framework import serializers

from accounts.models.parent import Parent


@final
class ParentSerializer(serializers.ModelSerializer[Parent]):
    @override
    @final
    class Meta:
        model = Parent
        fields = [
            "id",
            "account",
            "occupation",
            "office_address",
            "qualifications",
        ]


class ParentReadSerializer(serializers.ModelSerializer[Parent]):
    @final
    class Meta:
        model = Parent
        fields = [
            "id",
            "account",
            "occupation",
            "office_address",
            "qualifications",
        ]

# accounts/serializers.py
 
from typing import final, override
from rest_framework import serializers

from accounts.models import Account


@final
class AccountSerializer(serializers.ModelSerializer[Account]): 
    @override
    @final
    class Meta:
        model = Account
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email', 'address', 'school',
            'phone', 'whatsapp', 'is_active', 'is_approved', 'groups', 'user_permissions'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'groups': {'required': False},
            'user_permissions': {'required': False},
        }

class AccountReadSerializer(serializers.ModelSerializer[Account]):
    @final
    class Meta:
        model = Account
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email', 'phone', 'whatsapp',
            'classrooms', 'subjects'
        ]

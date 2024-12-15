# accounts/serializers.py
 
from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer): 
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



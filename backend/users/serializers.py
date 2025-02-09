# users/serializers.py

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'is_active', 'is_approved', 'is_staff', 'is_superuser',
            'account', 'school'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'full_name', 'email', "is_approved", "is_active"
        ]

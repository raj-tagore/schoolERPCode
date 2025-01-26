# users/serializers.py

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email',
            'is_active', 'is_approved', 'groups', 'permissions',
            'account'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }


class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'full_name', 'email', 'username', "is_approved", "is_active"
        ]

# users/serializers.py

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email', 'school',
            'is_active', 'is_approved', 'groups', 'user_permissions',
            'student_account', 'teacher_account', 'parent_account'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'groups': {'required': False},
            'user_permissions': {'required': False},
        }

class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'email',
            'classrooms', 'subjects', 'groups'
        ]

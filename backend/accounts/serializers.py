# accounts/serializers.py
from rest_framework import serializers
from timetable.serializers import TimeTableSerializer
from .models import Student, Teacher, Parent
from users.serializers import UserReadSerializer
from django.contrib.auth.models import Group, Permission

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name', 'codename']

class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'permissions']

class StudentSerializer(serializers.ModelSerializer):
    user_details = UserReadSerializer(source='user', read_only=True)
    group_details = GroupSerializer(source='group', read_only=True)
    
    class Meta:
        model = Student
        fields = '__all__'

class ParentSerializer(serializers.ModelSerializer):
    user_details = UserReadSerializer(source='user', read_only=True)
    group_details = GroupSerializer(source='group', read_only=True)
    children = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Parent
        fields = '__all__'

class BasicTeacherSerializer(serializers.ModelSerializer):
    user_details = UserReadSerializer(source='user', read_only=True)
    group_details = GroupSerializer(source='group', read_only=True)
    
    class Meta:
        model = Teacher
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    user_details = UserReadSerializer(source='user', read_only=True)
    group_details = GroupSerializer(source='group', read_only=True)
    timetable = TimeTableSerializer(source='subject', many=True, read_only=True)
    
    class Meta:
        model = Teacher
        fields = '__all__'
 


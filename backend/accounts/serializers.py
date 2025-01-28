# accounts/serializers.py
 
from rest_framework import serializers
from .models import Student, Teacher, Parent
from users.serializers import UserReadSerializer

class StudentSerializer(serializers.ModelSerializer):
    user_details = UserReadSerializer(source='user', read_only=True)
    class Meta:
        model = Student
        fields = '__all__'

class ParentSerializer(serializers.ModelSerializer):
    user_details = UserReadSerializer(source='user', read_only=True)
    class Meta:
        model = Parent
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    user_details = UserReadSerializer(source='user', read_only=True)
    class Meta:
        model = Teacher
        fields = '__all__'
 


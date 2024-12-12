# accounts/serializers.py

from rest_framework import serializers
from .models import Account
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth import authenticate
from tenants.models import CustomUser

class AccountSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Account
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email', 'address', 
            'phone', 'whatsapp', 'is_active', 'is_approved', 'standard', 'groups', 'user_permissions'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'groups': {'required': False},
            'user_permissions': {'required': False},
        }

class CustomUserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email',  
             'is_active', 'groups', 'user_permissions'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'groups': {'required': False},
            'user_permissions': {'required': False},
        }

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token
    
    def validate(self, attrs):

        # 'authenticate' checks all authentication backends in settings
        username = attrs.get("username")
        password = attrs.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Invalid credentials.")
        
        # Determine the user type
        if isinstance(user, CustomUser):
            type = 'internal'
        elif isinstance(user, Account):
            type = 'external'
        else:
            raise serializers.ValidationError("Invalid user type.")

        # Generate tokens
        refresh = self.get_token(user)
        refresh['type'] = type
        access = refresh.access_token
        access['type'] = type
             
        return {
            "refresh": str(refresh),
            "access": str(access),
            "type": type,
            "user_id": user.id, 
            "username": user.username,
        }
        
class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    
    def validate(self, attrs):

        # Call the superclass method to get the validated data
        data = super().validate(attrs)

        # Create access token and add 'type'
        refresh = RefreshToken(attrs['refresh'])
        access = refresh.access_token
        access['type'] = refresh['type']
        data['access'] = str(access)

        return data



# accounts/serializers.py

from rest_framework import serializers
from .models import Account
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User  # Default User model

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

    def create(self, validated_data):
        # Override create to handle password hashing
        account = Account(**validated_data)
        password = validated_data.pop('password', None)
        if password:
            account.set_password(password)
        account.save()
        return account

    def update(self, instance, validated_data):
        # Override update to handle password hashing if password is updated
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token
    
    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        # Calls `authenticate`, which checks all authentication backends in settings
        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Invalid credentials.")
        
        # Determine the user type
        if isinstance(user, User):
            table = 'user'
        elif isinstance(user, Account):
            table = 'account'
        else:
            raise serializers.ValidationError("Invalid user type.")

        # Generate tokens
        refresh = self.get_token(user)

        # Add custom claims
        refresh['table'] = table
            
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user_id": user.id, 
            "username": user.username,
        }
        
class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        # Call the superclass method to get the validated data
        data = super().validate(attrs)

        # Decode the refresh token to access custom claims
        refresh = RefreshToken(attrs['refresh'])

        # Create a new access token
        access_token = refresh.access_token

        # Add custom claims to the new access token
        # Copy over custom claims from the refresh token
        access_token['table'] = refresh['table']

        # Replace the access token in the response data
        data['access'] = str(access_token)

        return data

# accounts/views.py

from rest_framework import viewsets
from .models import Account
from rest_framework.permissions import DjangoModelPermissions
from .serializers import AccountSerializer, CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .permissions import AccountViewSetPermissions

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [AccountViewSetPermissions]


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer 
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tokens = serializer.validated_data

        # Send tokens in response body and set as cookies
        response = Response({"message": "Login successful", 
                             "user_id": tokens['user_id'], 
                             "username": tokens['username'],
                             "type": tokens['type'],
                             "access": tokens['access'],
                             "refresh": tokens['refresh']})

        return response

class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer
    
    def post(self, request, *args, **kwargs):

        # Extract the refresh token from cookies or auth header
        refresh = request.COOKIES.get('refresh')
        if not refresh:
            refresh = request.data['refresh']
        if not refresh:
            return Response({"error": "Refresh token not found in cookies"}, status=status.HTTP_400_BAD_REQUEST)

        # Manually set the refresh token in request.data to pass it to the serializer
        request.data['refresh'] = refresh
        serializer = self.get_serializer(data=request.data)
        
        # Validate and create a new access token
        serializer.is_valid(raise_exception=True)
        access = serializer.validated_data['access']

        # Set the new access token as an HttpOnly cookie, and send it back
        response = Response({"message": "Token refreshed successfully",
                             "access": access})

        return response

# Employee users

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [DjangoModelPermissions]   

# accounts/views.py

from rest_framework import viewsets
from .models import Account
from rest_framework.permissions import DjangoModelPermissions
from .serializers import AccountSerializer, CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [DjangoModelPermissions]   
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer 
    
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tokens = serializer.validated_data

        # Create a response object without including tokens in response data
        response = Response({"message": "Login successful", "user_id": tokens['user_id'], "username": tokens['username']})

        # Set the tokens as HttpOnly cookies
        response.set_cookie(
            key='access_token',
            value=tokens['access'],
            httponly=True,
            secure=False,  
            samesite='None',  
            max_age=60 * 15  
        )
        response.set_cookie(
            key='refresh_token',
            value=tokens['refresh'],
            httponly=True,
            secure=False,  
            samesite='None',
            max_age=60 * 60 * 24  
        )

        return response

class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer
    
    def post(self, request, *args, **kwargs):
        # Extract the refresh token from cookies
        refresh_token = request.COOKIES.get('refresh_token')
        if not refresh_token:
            return Response({"error": "Refresh token not found in cookies"}, status=status.HTTP_400_BAD_REQUEST)

        # Manually set the refresh token in request.data to pass it to the serializer
        request.data['refresh'] = refresh_token
        serializer = self.get_serializer(data=request.data)
        
        # Validate and create a new access token
        serializer.is_valid(raise_exception=True)
        access_token = serializer.validated_data['access']

        # Set the new access token as an HttpOnly cookie
        response = Response({"message": "Token refreshed successfully"})
        response.set_cookie(
            key='access_token',
            value=access_token,
            httponly=True,
            secure=False,  
            samesite='None',
            max_age=60 * 15  
        )
        return response

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed, InvalidToken
from django.contrib.auth.models import User
from accounts.models import Account

class CookieJWTAuthentication(JWTAuthentication):

    def get_user(self, validated_token):

        # Get user type
        type = validated_token.get('type')
        if type == 'internal':
            user_model = User
        elif type == 'external':
            user_model = Account
        else:
            raise AuthenticationFailed('Invalid user type')

        # get user id
        user_id = validated_token.get('user_id')
        if user_id is None:
            raise InvalidToken('Token contained no recognizable user identification')

        # get user
        try:
            user = user_model.objects.get(id=user_id)
        except user_model.DoesNotExist:
            raise AuthenticationFailed('User not found')

        if not user.is_active:
            raise AuthenticationFailed('User is inactive')

        return user 
    
    def authenticate(self, request):
        
        # Look for the token in the cookie and auth header
        access = request.COOKIES.get('access')
        if not access:
            auth_header = request.headers.get('Authorization')
            if auth_header and auth_header.startswith('Bearer '):
                access = auth_header.split(' ')[1] 

        if access:
            validated_token = self.get_validated_token(access)
            return self.get_user(validated_token), validated_token

        # Fall back to the default behavior (Authorization header)
        return super().authenticate(request)
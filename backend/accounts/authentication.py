from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed, InvalidToken
from django.contrib.auth.models import User
from accounts.models import Account

class CookieJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        table = validated_token.get('table')
        
        if table == 'user':
            user_model = User
        elif table == 'account':
            user_model = Account
        else:
            raise AuthenticationFailed('Invalid user type')

        user_id = validated_token.get('user_id')
        if user_id is None:
            raise InvalidToken('Token contained no recognizable user identification')

        try:
            user = user_model.objects.get(id=user_id)
        except user_model.DoesNotExist:
            raise AuthenticationFailed('User not found')

        if not user.is_active:
            raise AuthenticationFailed('User is inactive')

        return user
    
    def authenticate(self, request):
        
        # Look for the token in the 'access_token' cookie
        access_token = request.COOKIES.get('access_token')
        if access_token:
            # If a token is found in the cookie, treat it as the token
            validated_token = self.get_validated_token(access_token)
            return self.get_user(validated_token), validated_token

        # Fall back to the default behavior (Authorization header)
        return super().authenticate(request)
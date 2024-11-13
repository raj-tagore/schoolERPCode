from rest_framework_simplejwt.authentication import JWTAuthentication

class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        # Look for the token in the 'access_token' cookie
        access_token = request.COOKIES.get('access_token')
        print("access_token", access_token)
        if access_token:
            # If a token is found in the cookie, treat it as the token
            validated_token = self.get_validated_token(access_token)
            return self.get_user(validated_token), validated_token

        # Fall back to the default behavior (Authorization header)
        return super().authenticate(request)
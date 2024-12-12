from django.contrib.auth.backends import BaseBackend
from tenants.models import CustomUser 

# custom backend to enable logging in to admin using CustomUser
class CustomUserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Authenticate using CustomUser
            user = CustomUser.objects.get(username=username)
            if user.check_password(password):  # Ensure passwords are hashed and checked properly
                return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
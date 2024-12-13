from django.contrib.auth.backends import BaseBackend
from .models import Account 
from django.db import ProgrammingError

# custom backend to enable logging in to admin using Account
class CustomUserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Authenticate using Account
            user = Account.objects.get(username=username)
            if user.check_password(password):  # Ensure passwords are hashed and checked properly
                return user
        except Account.DoesNotExist:
            return None
        except ProgrammingError:
            return None

    def get_user(self, user_id):
        try:
            return Account.objects.get(pk=user_id)
        except Account.DoesNotExist:
            return None
from django.contrib.auth.backends import ModelBackend
from .models import Account  
from django.db.utils import ProgrammingError

class AccountsAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Account.objects.get(username=username)  
            if user.check_password(password):  
                return user
        except Account.DoesNotExist:
            return None
        except ProgrammingError as e:
            print("Database error in CustomModelBackend:", e)
            return None
        except Exception as e:
            print("Unexpected error in CustomModelBackend:", e)
            return None
        return None 
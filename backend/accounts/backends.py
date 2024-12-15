from django.contrib.auth.backends import BaseBackend
from .models import Account
from django.core.exceptions import PermissionDenied
from django.http import Http404
from rest_framework.exceptions import AuthenticationFailed

class TenantAwareAuthBackend(BaseBackend):
    def authenticate(self, request, username = ..., password = ..., **kwargs):

        tenant = getattr(request, 'tenant', None)
        if not tenant:
            raise Http404('tenant not given')
        user = Account.objects.get(username=username)
        if user.check_password(password):
            if user.school == tenant or str(user.school) == 'public':
                return None
            raise PermissionDenied('User and School mismatch')
        raise AuthenticationFailed('Wrong Credentials')

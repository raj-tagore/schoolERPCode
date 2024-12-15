# accounts/views.py

from rest_framework import viewsets
from .models import Account
from .serializers import AccountSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class GetProfile(RetrieveAPIView):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
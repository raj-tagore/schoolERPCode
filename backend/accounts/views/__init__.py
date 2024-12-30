# accounts/views.py
from typing import final, override
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
    ListAPIView,
    CreateAPIView,
)

from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from accounts.models import Account
from accounts.permissions import AccountPermissions
from accounts.serializers import AccountReadSerializer, AccountSerializer


@final
class AllAccounts(ListAPIView[Account]):
    queryset = Account.objects.all()
    serializer_class = AccountReadSerializer
    permission_classes = [IsAuthenticated]

    @override
    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        id = request.query_params.get("id")
        fname = request.query_params.get("fname")
        lname = request.query_params.get("lname")
        group = request.query_params.get("group")


        if id:
            queryset = queryset.filter(id=id)
        if fname:
            queryset = queryset.filter(fname__icontains=fname)
        if lname:
            queryset = queryset.filter(lname__icontains=lname)
        if group:
            queryset = queryset.filter(groups__id=group)

        return queryset


@final
class AnyAccount(RetrieveUpdateDestroyAPIView[Account]):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated, AccountPermissions]
    queryset = Account.objects.all()
    lookup_field = "id"

@final
class SelfAccount(RetrieveUpdateDestroyAPIView[Account]):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    @override
    def get_object(self):
        return self.request.user



@final
class ReadAccount(RetrieveAPIView[Account]):
    serializer_class = AccountReadSerializer
    permission_classes = [IsAuthenticated]
    queryset = Account.objects.all()
    lookup_field = "id"

@final
class CreateAccount(CreateAPIView[Account]):
    serializer_class = AccountSerializer
    permission_classes = [DjangoModelPermissions]

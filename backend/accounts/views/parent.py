# accounts/views.py
from typing import final, override
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
    ListAPIView,
    CreateAPIView,
)

from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from accounts.models.parent import Parent
from accounts.permissions.parent import ParentPermissions
from accounts.serializers.parent import ParentReadSerializer, ParentSerializer


@final
class AllParents(ListAPIView[Parent]):
    queryset = Parent.objects.all()
    serializer_class = ParentReadSerializer
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
class AnyParent(RetrieveUpdateDestroyAPIView[Parent]):
    serializer_class = ParentSerializer
    permission_classes = [IsAuthenticated, ParentPermissions]
    queryset = Parent.objects.all()
    lookup_field = "id"


@final
class ReadParent(RetrieveAPIView[Parent]):
    serializer_class = ParentReadSerializer
    permission_classes = [IsAuthenticated]
    queryset = Parent.objects.all()
    lookup_field = "id"

@final
class CreateParent(CreateAPIView[Parent]):
    serializer_class = ParentSerializer
    permission_classes = [DjangoModelPermissions]

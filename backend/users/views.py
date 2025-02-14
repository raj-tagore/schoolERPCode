# users/views.py

from .models import User
from .serializers import UserSerializer, UserReadSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .permissions import UserPermissions
from django.db.models import Q

from schoolERPCode.viewsets import get_standard_model_viewset


def user_filter(self, queryset, **kwargs):
    if "fname" in kwargs:
        queryset = queryset.filter(fname__icontains=kwargs["fname"])
    if "lname" in kwargs:
        queryset = queryset.filter(lname__icontains=kwargs["lname"])
    if "name" in kwargs:
        queryset = queryset.filter(
            Q(first_name__icontains=kwargs["name"])
            | Q(last_name__icontains=kwargs["name"])
        )
    if "group" in kwargs:
        queryset = queryset.filter(groups__id=kwargs["group"])
    return queryset


users_viewset = get_standard_model_viewset(
    queryset=User.objects.all(),
    serializer_class=UserSerializer,
    basic_serializer_class=UserReadSerializer,
    permission_class=UserPermissions,
    filter_queryset=user_filter,
)


class SelfUser(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class ReadUser(RetrieveAPIView):
    serializer_class = UserReadSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    lookup_field = "id"


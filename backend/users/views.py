# users/views.py

from .models import User
from .serializers import UserSerializer, UserReadSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .permissions import UserPermissions
from django.db.models import Q

from schoolERPCode.viewsets import get_standard_model_viewset

def user_filter(self, queryset, fname, lname, name, group):
    if fname:
        queryset = queryset.filter(fname__icontains=fname)
    if lname:
        queryset = queryset.filter(lname__icontains=lname)
    if name:
        queryset = queryset.filter(
            Q(first_name__icontains=name) | Q(last_name__icontains=name)
        )
    if group:
        queryset = queryset.filter(groups__id=group)
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
    lookup_field = 'id'


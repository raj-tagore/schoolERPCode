# users/views.py

from .models import User
from .serializers import UserSerializer, UserReadSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .permissions import UserPermissions

class AllUsers(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserReadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        id = request.query_params.get('id')
        fname = request.query_params.get('fname')
        lname = request.query_params.get('lname')
        group = request.query_params.get('group')

        if id:
            queryset = queryset.filter(id=id)
        if fname:
            queryset = queryset.filter(fname__icontains=fname)
        if lname:
            queryset = queryset.filter(lname__icontains=lname)
        if group:
            queryset = queryset.filter(groups__id=group)

        return queryset

class AnyUser(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, UserPermissions]
    queryset = User.objects.all()
    lookup_field = 'id'

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

class CreateUser(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [DjangoModelPermissions]


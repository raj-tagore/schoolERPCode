# accounts/views.py

from .models import Account
from .serializers import AccountSerializer, AccountReadSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .permissions import AccountPermissions

class AllAccounts(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountReadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        id = request.query_params.get('id')
        fname = request.query_params.get('fname')
        lname = request.query_params.get('lname')
        classroom = request.query_params.get('classroom') 
        subject = request.query_params.get('subject') 

        if id:
            queryset = queryset.filter(id=id)
        if fname:
            queryset = queryset.filter(fname__icontains=fname)
        if lname:
            queryset = queryset.filter(lname__icontains=lname)
        if classroom:
            queryset = queryset.filter(classrooms__id=classroom)
        if subject:
            queryset = queryset.filter(subjects__id=subject)

        return queryset

class AnyAccount(RetrieveUpdateDestroyAPIView):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated, AccountPermissions]
    queryset = Account.objects.all()
    lookup_field = 'id'

class SelfAccount(RetrieveUpdateDestroyAPIView):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
class ReadAccount(RetrieveAPIView):
    serializer_class = AccountReadSerializer
    permission_classes = [IsAuthenticated]
    queryset = Account.objects.all()
    lookup_field = 'id'

class CreateAccount(CreateAPIView):
    serializer_class = AccountSerializer
    permission_classes = [DjangoModelPermissions]
# accounts/views.py
from typing import override
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
    ListAPIView,
    CreateAPIView,
)
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from accounts.models import Account
from accounts.models.student import Student
from accounts.permissions import AccountPermissions
from accounts.serializers import AccountReadSerializer, AccountSerializer


class AllStudents(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentReadSerializer
    permission_classes = [IsAuthenticated]

    @override
    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        id = request.query_params.get("id")
        account = request.query_params.get("account")
        roll_no = request.query_params.get("roll_no")
        classroom = request.query_params.get("classroom")
        guardian1 = request.query_params.get("guardian1")
        guardian2 = request.query_params.get("guardian2")
        identity_proof_type = request.query_params.get("identity_proof_type")

        if id:
            queryset = queryset.filter(id=id)
        if account:
            queryset = queryset.filter(account__id=account)
        if roll_no:
            queryset = queryset.filter(roll_no=roll_no)
        if classroom:
            queryset = queryset.filter(classroom__id=classroom)
        if guardian1:
            queryset = queryset.filter(guardian1__id=guardian1)
        if guardian2:
            queryset = queryset.filter(guardian2__id=guardian2)
        if identity_proof_type:
            queryset = queryset.filter(identity_proof_type=identity_proof_type)

        return queryset


class AnyStudent(RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated, StudentPermissions]
    queryset = Student.objects.all()
    lookup_field = "id"


class SelfStudent(RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.student_info


class ReadStudent(RetrieveAPIView):
    serializer_class = StudentReadSerializer
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    lookup_field = "id"


class CreateStudent(CreateAPIView):
    serializer_class = StudentSerializer
    permission_classes = [DjangoModelPermissions]

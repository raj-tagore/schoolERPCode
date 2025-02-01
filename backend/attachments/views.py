# myapp/views.py

from attachments.permissions import AttachmentPermissions
from .serializers import AttachmentSerializer
from .models import Attachment
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    CreateAPIView,
)


class AllAttachments(ListAPIView):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        id = request.query_params.get("id")
        name = request.query_params.get("name")
        is_active = request.query_params.get("is_active")
        created_at = request.query_params.get("created_at")
        updated_at = request.query_params.get("updated_at")
        additional_info = request.query_params.get("additional_info")

        if id:
            queryset = queryset.filter(id=id)
        if name:
            queryset = queryset.filter(name__icontains=name)
        if is_active:
            queryset = queryset.filter(is_active=is_active)
        if created_at:
            queryset = queryset.filter(created_at=created_at)
        if updated_at:
            queryset = queryset.filter(updated_at=updated_at)
        if additional_info:
            queryset = queryset.filter(additional_info__icontains=additional_info)

        return queryset


class AnyAttachment(RetrieveUpdateDestroyAPIView):
    serializer_class = AttachmentSerializer
    permission_classes = [IsAuthenticated, AttachmentPermissions]
    queryset = Attachment.objects.all()
    lookup_field = "id"


class CreateAttachment(CreateAPIView):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [DjangoModelPermissions]

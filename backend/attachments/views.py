# myapp/views.py
from .serializers import AttachmentSerializer
from .models import Attachment

from schoolERPCode.viewsets import get_standard_model_viewset


def attachment_filter(self, queryset, **kwargs):
    if "id" in kwargs:
        queryset = queryset.filter(id=kwargs["id"])
    if "name" in kwargs:
        queryset = queryset.filter(name__icontains=kwargs["name"])
    if "is_active" in kwargs:
        queryset = queryset.filter(is_active=kwargs["is_active"])
    if "created_at_start" in kwargs:
        queryset = queryset.filter(created_at__gte=kwargs["created_at_start"])
    if "created_at_end" in kwargs:
        queryset = queryset.filter(created_at__lte=kwargs["created_at_end"])
    if "updated_at_start" in kwargs:
        queryset = queryset.filter(updated_at__gte=kwargs["updated_at_start"])
    if "updated_at_end" in kwargs:
        queryset = queryset.filter(updated_at__lte=kwargs["updated_at_end"])
    if "additional_info" in kwargs:
        queryset = queryset.filter(additional_info__icontains=kwargs["additional_info"])

    return queryset


attachments_viewset = get_standard_model_viewset(
    queryset=Attachment.objects.all(),
    serializer_class=AttachmentSerializer,
    filter_queryset=attachment_filter,
    basic_serializer_class=AttachmentSerializer,
)

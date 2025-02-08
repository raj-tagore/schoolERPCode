# myapp/views.py
from .serializers import AttachmentSerializer
from .models import Attachment

from schoolERPCode.viewsets import get_standard_model_viewset

def attachment_filter(self, queryset, id, name, is_active, created_at_start, created_at_end, updated_at_start, updated_at_end, additional_info):
    if id:
        queryset = queryset.filter(id=id)
    if name:
        queryset = queryset.filter(name__icontains=name)
    if is_active:
        queryset = queryset.filter(is_active=is_active)
    if created_at_start:
        queryset = queryset.filter(created_at__gte=created_at_start)
    if created_at_end:
        queryset = queryset.filter(created_at__lte=created_at_end)
    if updated_at_start:
        queryset = queryset.filter(updated_at__gte=updated_at_start)
    if updated_at_end:
        queryset = queryset.filter(updated_at__lte=updated_at_end)
    if additional_info:
        queryset = queryset.filter(additional_info__icontains=additional_info)

    return queryset

attachment_viewset = get_standard_model_viewset(
    queryset=Attachment.objects.all(),
    serializer_class=AttachmentSerializer,
    filter_queryset=attachment_filter,
    basic_serializer_class=AttachmentSerializer,
)

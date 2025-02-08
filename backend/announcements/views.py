# announcements/views.py

from .models import Announcement
from .serializers import AnnouncementSerializer
from .permissions import AnnouncementPermissions

from schoolERPCode.viewsets import get_standard_model_viewset


def filter_announcements(
    self, queryset, id, title, classroom, subject, is_school_wide, signed_by
):
    if id:
        queryset = queryset.filter(id=id)
    if title:
        queryset = queryset.filter(title__icontains=title)
    if classroom:
        queryset = queryset.filter(classrooms__id=classroom)
    if subject:
        queryset = queryset.filter(subjects__id=subject)
    if is_school_wide:
        queryset = queryset.filter(is_school_wide=is_school_wide)
    if signed_by:
        queryset = queryset.filter(signed_by__id=signed_by)

    return queryset


announcement_viewset = get_standard_model_viewset(
    queryset=Announcement.objects.all(),
    serializer_class=AnnouncementSerializer,
    filter_queryset=filter_announcements,
    basic_serializer_class=AnnouncementSerializer,
    permission=AnnouncementPermissions,
)

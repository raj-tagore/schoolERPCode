# announcements/views.py

from .models import Announcement
from .serializers import AnnouncementSerializer
from .permissions import AnnouncementPermissions

from schoolERPCode.viewsets import get_standard_model_viewset


def filter_announcements(self, queryset, **kwargs):
    print(kwargs)
    if "id" in kwargs:
        queryset = queryset.filter(id=kwargs["id"])
    if "title" in kwargs:
        queryset = queryset.filter(title__icontains=kwargs["title"])
    if "classroom" in kwargs:
        queryset = queryset.filter(classrooms__id=kwargs["classroom"])
    if "subject" in kwargs:
        queryset = queryset.filter(subjects__id=kwargs["subject"])
    if "is_school_wide" in kwargs:
        queryset = queryset.filter(is_school_wide=kwargs["is_school_wide"])
    if "signed_by" in kwargs:
        queryset = queryset.filter(signed_by__id=kwargs["signed_by"])

    return queryset


announcement_viewset = get_standard_model_viewset(
    queryset=Announcement.objects.all(),
    serializer_class=AnnouncementSerializer,
    filter_queryset=filter_announcements,
    basic_serializer_class=AnnouncementSerializer,
    permission_class=AnnouncementPermissions,
)

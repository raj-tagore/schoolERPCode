# announcements/views.py

from .models import Announcement
from .serializers import AnnouncementSerializer
from .permissions import AnnouncementPermissions

import datetime
from schoolERPCode.viewsets import get_standard_model_viewset


def filter_announcements(self, queryset, **kwargs):
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
    if "is_released" in kwargs and kwargs["is_released"] == "True":
        queryset = queryset.filter(release_at__lte=datetime.datetime.now())
    if "is_expired" in kwargs and kwargs["is_expired"] == "True":
        queryset = queryset.filter(expiry_at__lte=datetime.datetime.now())

    return queryset


announcement_viewset = get_standard_model_viewset(
    queryset=Announcement.objects.all(),
    serializer_class=AnnouncementSerializer,
    filter_queryset=filter_announcements,
    basic_serializer_class=AnnouncementSerializer,
    permission_class=AnnouncementPermissions,
)

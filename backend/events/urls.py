from django.urls import path, include
from .views import (
    events_viewset,
    Calendar,
)

urlpatterns = [
    path("", include(events_viewset)),
    path("calendar/", Calendar.as_view(), name="calendar"),
]

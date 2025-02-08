from django.urls import path, include
from .views import (
    AllEvents,
    AnyEvent,
    CreateEvent,
    calendars_viewset,
)

urlpatterns = [
    path("calendar/", include(calendars_viewset)),
    path("all/", AllEvents.as_view()),
    path("<int:id>/", AnyEvent.as_view()),
    path("create/", CreateEvent.as_view()),
]

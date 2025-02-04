from django.urls import path
from .views import AllCalendars, AllEvents, AnyCalendar, AnyEvent, CreateCalendar, CreateEvent

urlpatterns = [
    path("calendar/all/", AllCalendars.as_view()),
    path("calendar/<int:id>/", AnyCalendar.as_view()),
    path("calendar/create/", CreateCalendar.as_view()),
    path("all/", AllEvents.as_view()),
    path("<int:id>/", AnyEvent.as_view()),
    path("create/", CreateEvent.as_view()),
]

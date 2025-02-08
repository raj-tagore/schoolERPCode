from django.urls import path, include

from timetable.views import periods_viewset, timetable_viewset 

urlpatterns = [
    path("period/", include(periods_viewset)),
    path("", include(timetable_viewset)),
]

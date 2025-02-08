from django.urls import path, include

from timetable.views import period_viewset, timetable_viewset 

urlpatterns = [
    path("period/", include(period_viewset)),
    path("", include(timetable_viewset)),
]

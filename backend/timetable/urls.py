from django.urls import path

from timetable.views import AllPeriods, AllTimeTables, AnyPeriod, AnyTimeTable, CreatePeriod, CreateTimeTable

urlpatterns = [
    path("period/all/", AllPeriods.as_view()),
    path("period/<int:id>/", AnyPeriod.as_view()),
    path("period/create/", CreatePeriod.as_view()),
    path("timetable/all/", AllTimeTables.as_view()),
    path("timetable/<int:id>/", AnyTimeTable.as_view()),
    path("timetable/create/", CreateTimeTable.as_view()),
]

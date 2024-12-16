from django.urls import path
from .views import (
    AllClassrooms,
    AnyClassroom,
    CreateClassroom,
    AllSubjects,
    AnySubject,
    CreateSubject,
)

urlpatterns = [
    path("classroom/all/", AllClassrooms.as_view()),
    path("classroom/<int:id>/", AnyClassroom.as_view()),
    path("classroom/create/", CreateClassroom.as_view()),
    path("subject/all", AllSubjects.as_view()),
    path("subject/<int:id>/", AnySubject.as_view()),
    path("subject/create/", CreateSubject.as_view()),
]

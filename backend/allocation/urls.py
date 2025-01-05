from django.urls import path
from .views import (
    AllClassrooms,
    AnyClassroom,
    ClassroomJoinLinksView,
    CreateClassroom,
    AllSubjects,
    AnySubject,
    CreateSubject,
)

urlpatterns = [
    path("classrooms/all/", AllClassrooms.as_view()),
    path("classrooms/<int:id>/", AnyClassroom.as_view()),
    path("classrooms/create/", CreateClassroom.as_view()),
    path("classroom/join_link/", ClassroomJoinLinksView.as_view()),
    path("subjects/all/", AllSubjects.as_view()),
    path("subjects/<int:id>/", AnySubject.as_view()),
    path("subjects/create/", CreateSubject.as_view()),
]

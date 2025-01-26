from django.urls import path
from .views import (
    AllClassrooms,
    AnyClassroom,
    CreateClassroom,
    AllSubjects,
    AnySubject,
    CreateSubject,
    JoinClassroomView,
)

urlpatterns = [
    path("classrooms/all/", AllClassrooms.as_view()),
    path("classrooms/<int:id>/", AnyClassroom.as_view()),
    path("classrooms/create/", CreateClassroom.as_view()),
    path("classrooms/join/<uuid:join_code>", JoinClassroomView.as_view()),
    path("subjects/all/", AllSubjects.as_view()),
    path("subjects/<int:id>/", AnySubject.as_view()),
    path("subjects/create/", CreateSubject.as_view()),
]

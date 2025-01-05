from django.urls import include, path
from .views import (
    AllClassrooms,
    AnyClassroom,
    ClassroomJoinLinksView,
    CreateClassroom,
    AllSubjects,
    AnySubject,
    CreateSubject,
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"join_link", ClassroomJoinLinksView)

urlpatterns = [
    path("/classrooms/", include(router.urls)),
    path("classrooms/all/", AllClassrooms.as_view()),
    path("classrooms/<int:id>/", AnyClassroom.as_view()),
    path("classrooms/create/", CreateClassroom.as_view()),
    path("subjects/all/", AllSubjects.as_view()),
    path("subjects/<int:id>/", AnySubject.as_view()),
    path("subjects/create/", CreateSubject.as_view()),
]

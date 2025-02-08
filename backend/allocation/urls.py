from django.urls import path, include
from .views import (
    classroom_viewset,
    subject_viewset,
    JoinClassroomView,
)

urlpatterns = [
    path("classrooms/", include(classroom_viewset)),
    path("subjects/", include(subject_viewset)),
    path("classrooms/join/<uuid:join_code>", JoinClassroomView.as_view()),
]

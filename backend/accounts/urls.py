from django.urls import path, include
from .views import (
    parent_viewset,
    teacher_viewset,
    student_viewset,
    ParentStats,
    TeacherStats,
    StudentStats,
)

urlpatterns = [
    # -- PARENT --
    path("parents/", include(parent_viewset)),
    path("parents/stats/", ParentStats.as_view(), name="parent-stats"),
    # -- TEACHER --
    path("teachers/", include(teacher_viewset)),
    path("teachers/stats/", TeacherStats.as_view(), name="teacher-stats"),
    # -- STUDENT --
    path("students/", include(student_viewset)),
    path("students/stats/", StudentStats.as_view(), name="student-stats"),
]


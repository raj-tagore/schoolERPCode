from django.urls import path
from .views import (
    AnyParent, CreateParent,
    AnyTeacher, CreateTeacher,
    AnyStudent, CreateStudent
)

urlpatterns = [
    # -- PARENT --
    path('parent/<int:id>/', AnyParent.as_view(), name='any-parent'),
    path('parent/create/', CreateParent.as_view(), name='create-parent'),

    # -- TEACHER --
    path('teacher/<int:id>/', AnyTeacher.as_view(), name='any-teacher'),
    path('teacher/create/', CreateTeacher.as_view(), name='create-teacher'),

    # -- STUDENT --
    path('student/<int:id>/', AnyStudent.as_view(), name='any-student'),
    path('student/create/', CreateStudent.as_view(), name='create-student'),
]
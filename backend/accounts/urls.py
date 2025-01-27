from django.urls import path
from .views import (
    AllParents, AnyParent, CreateParent, ParentStats,
    AllTeachers, AnyTeacher, CreateTeacher, TeacherStats,
    AllStudents, AnyStudent, CreateStudent, StudentStats
)

urlpatterns = [
    # -- PARENT --
    path('parents/all/', AllParents.as_view(), name='all-parents'),
    path('parents/<int:id>/', AnyParent.as_view(), name='any-parent'),
    path('parents/create/', CreateParent.as_view(), name='create-parent'),
    path('parents/stats/', ParentStats.as_view(), name='parent-stats'),

    # -- TEACHER --
    path('teachers/all/', AllTeachers.as_view(), name='all-teachers'),
    path('teachers/<int:id>/', AnyTeacher.as_view(), name='any-teacher'),
    path('teachers/create/', CreateTeacher.as_view(), name='create-teacher'),
    path('teachers/stats/', TeacherStats.as_view(), name='teacher-stats'),

    # -- STUDENT --
    path('students/all/', AllStudents.as_view(), name='all-students'),
    path('students/<int:id>/', AnyStudent.as_view(), name='any-student'),
    path('students/create/', CreateStudent.as_view(), name='create-student'),
    path('students/stats/', StudentStats.as_view(), name='student-stats'),
]
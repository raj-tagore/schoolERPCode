from django.contrib import admin
from django.urls import path, include

from accounts.views.parent import AllParents, AnyParent, CreateParent, ReadParent
from accounts.views.student import AllStudents, AnyStudent, CreateStudent, ReadStudent
from accounts.views.teacher import AllTeachers, AnyTeacher, CreateTeacher, ReadTeacher
from .views import AllAccounts, SelfAccount, ReadAccount, CreateAccount, AnyAccount


teacher_url_patterns = [
    path("all/", AllTeachers.as_view()),
    path("<int:id>/", AnyTeacher.as_view()),
    path("read/", ReadTeacher.as_view()),
    path("create/", CreateTeacher.as_view()),
]

student_url_patterns = [
    path("all/", AllStudents.as_view()),
    path("<int:id>/", AnyStudent.as_view()),
    path("read/", ReadStudent.as_view()),
    path("create/", CreateStudent.as_view()),
]

parent_url_patterns = [
    path("all/", AllParents.as_view()),
    path("<int:id>/", AnyParent.as_view()),
    path("read/", ReadParent.as_view()),
    path("create/", CreateParent.as_view()),
]

urlpatterns = [
    path("all/", AllAccounts.as_view()),
    path("<int:id>/", AnyAccount.as_view()),
    path("self/", SelfAccount.as_view()),
    path("read/", ReadAccount.as_view()),
    path("create/", CreateAccount.as_view()),
    path("teacher/", include(teacher_url_patterns)),
    path("student/", include(student_url_patterns)),
    path("parent/", include(parent_url_patterns)),
]

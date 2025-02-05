from django.urls import path
from .views import (
    AllAssessments,
    AnyAssessment,
    CreateAssessment,
    AllStudentAssessments,
    AnyStudentAssessment,
    CreateStudentAssessment,
)

urlpatterns = [
    path("submitted/all/", AllStudentAssessments.as_view()),
    path("submitted/<int:id>/", AnyStudentAssessment.as_view()),
    path("submitted/create/", CreateStudentAssessment.as_view()),
    path("all/", AllAssessments.as_view()),
    path("<int:id>/", AnyAssessment.as_view()),
    path("create/", CreateAssessment.as_view()),
]

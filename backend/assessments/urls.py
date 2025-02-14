from django.urls import path, include
from .views import (
    assessment_viewset,
    student_assessment_viewset,
)

urlpatterns = [
    path("submitted/", include(student_assessment_viewset)),
    path("", include(assessment_viewset)),
]

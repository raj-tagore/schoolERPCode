from django.urls import path, include
from .views import (
    AllAssignments,
    AnyAssignments,
    CreateAssignment,
    MarkSubmittedAssignment,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"", MarkSubmittedAssignment)

urlpatterns = [
    path("mark/", include(router.urls)),
    path("all/", AllAssignments.as_view()),
    path("<int:id>/", AnyAssignments.as_view()),
    path("create/", CreateAssignment.as_view()),
]

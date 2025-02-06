from django.urls import path, include
from .views import (
    assignment_viewset,
    MarkSubmittedAssignment,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"", MarkSubmittedAssignment)

urlpatterns = [
    path("mark/", include(router.urls)),
]

urlpatterns.extend(
    assignment_viewset
)

from django.urls import path, include
from .views import (
    events_viewset,
)

urlpatterns = [
    path("", include(events_viewset)),
]

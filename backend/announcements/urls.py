from django.urls import path, include
from .views import announcement_viewset

urlpatterns = [
    path("", include(announcement_viewset))
]

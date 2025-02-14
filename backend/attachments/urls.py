# myapp/urls.py

from django.urls import path, include
from .views import attachments_viewset

urlpatterns = [
    path("", include(attachments_viewset)),
]

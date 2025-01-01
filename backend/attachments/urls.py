# myapp/urls.py

from django.urls import path
from .views import AttachmentUploadView

urlpatterns = [
    path('upload/', AttachmentUploadView.as_view(), name='attachment-upload'),
]

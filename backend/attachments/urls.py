# myapp/urls.py

from django.urls import path
from .views import AllAttachments, AnyAttachment, CreateAttachment

urlpatterns = [
    path("all/", AllAttachments.as_view()),
    path("<int:id>/", AnyAttachment.as_view()),
    path("create/", CreateAttachment.as_view()),
]

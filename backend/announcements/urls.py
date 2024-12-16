from django.contrib import admin
from django.urls import path, include
from .views import AllAnnouncements, AnyAnnouncement, CreateAnnouncement

urlpatterns = [
    path("all/", AllAnnouncements.as_view()),
    path("<int:id>/", AnyAnnouncement.as_view()),
    path("create/", CreateAnnouncement.as_view()),
]

from django.contrib import admin
from django.urls import path, include
from .views import AllEvents, AnyEvent, CreateEvent

urlpatterns = [
    path("all/", AllEvents.as_view()),
    path("<int:id>/", AnyEvent.as_view()),
    path("create/", CreateEvent.as_view()),
]

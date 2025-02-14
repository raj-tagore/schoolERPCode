from django.urls import path, include
from .views import attendance_report_views

urlpatterns = [
    path('attendance/', include(attendance_report_views)),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClassroomViewSet, SubjectViewSet

router = DefaultRouter()
router.register(r'classrooms', ClassroomViewSet)
router.register(r'subjects', SubjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

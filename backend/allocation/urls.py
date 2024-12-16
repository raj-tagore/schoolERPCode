from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AllClassroom, AnyClassroom, CreateClassroom, AllSubjects, AnySubjects, CreateSubject

classroom_router = DefaultRouter()

classroom_router.register('all/', AllClassrooms)
classroom_router.register('<int:id>/', AnyClassroom)
classroom_router.register('create/', CreateClassroom)

subject_router = DefaultRouter()

subject_router.register('all/', AllSubjects)
subject_router.register('<int:id>/', AnySubject)
subject_router.register('create/', CreateSubject)

urlpatterns = [
    path('classroom', include(classroom_router.urls)),
    path('subject', include(subject_router.urls))
]

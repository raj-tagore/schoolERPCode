from django.contrib import admin
from django.urls import path, include
from .views import AllUsers, SelfUser, ReadUser, CreateUser, AnyUser


urlpatterns = [
    path('all/', AllUsers.as_view()),
    path('<int:id>/', AnyUser.as_view()),
    path('self/', SelfUser.as_view()),
    path('read/', ReadUser.as_view()),
    path('create/', CreateUser.as_view()),
]

    

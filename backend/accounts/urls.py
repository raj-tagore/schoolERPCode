from unfold.admin import ModelAdmin
from django.contrib import admin
from django.urls import path, include
from .views import AllAccounts, SelfAccount, ReadAccount, CreateAccount, AnyAccount


urlpatterns = [
    path('all/', AllAccounts.as_view()),
    path('<int:id>/', AnyAccount.as_view()),
    path('self/', SelfAccount.as_view()),
    path('read/', ReadAccount.as_view()),
    path('create/', CreateAccount.as_view()),
]

    

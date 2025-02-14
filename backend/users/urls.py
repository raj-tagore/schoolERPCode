from django.urls import path, include
from .views import SelfUser, ReadUser, users_viewset


urlpatterns = [
    path('self/', SelfUser.as_view()),
    path('read/', ReadUser.as_view()),
    path('', include(users_viewset)),
]

    

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet, GetProfile

router = DefaultRouter()
router.register(r'', AccountViewSet)


urlpatterns = [
    path('all/', include(router.urls)),
    path('self/', GetProfile.as_view())
]

    

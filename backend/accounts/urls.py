from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.views import AccountViewSet

router = DefaultRouter()
router.register(r'', AccountViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

    
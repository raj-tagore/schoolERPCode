from django.shortcuts import render
from .models import Announcement
from .serializers import AnnouncementSerializer
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
# Create your views here.

class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


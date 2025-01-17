# announcements/views.py

from django.shortcuts import render
from .models import Announcement
from .serializers import AnnouncementSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from .permissions import AnnouncementPermissions


class AllAnnouncements(ListAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        id = request.query_params.get('id')
        title = request.query_params.get('title')
        classroom = request.query_params.get('classroom') 
        subject = request.query_params.get('subject') 
        students = request.query_params.get('students') 
        teachers = request.query_params.get('other_teachers') 

        if id:
            queryset = queryset.filter(id=id)
        if title:
            queryset = queryset.filter(title__icontains=title)
        if classroom:
            queryset = queryset.filter(classrooms__id=classroom)
        if subject:
            queryset = queryset.filter(subjects__id=subject)
        if students:
            queryset = queryset.filter(classrooms__students__id__in=[students]).distinct()
        if teachers:
            queryset = queryset.filter(classrooms__other_teachers__id__in=[teachers]).distinct()

        return queryset

class AnyAnnouncement(RetrieveUpdateDestroyAPIView):
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAuthenticated, AnnouncementPermissions]
    queryset = Announcement.objects.all()
    lookup_field = 'id'

class CreateAnnouncement(CreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [DjangoModelPermissions]


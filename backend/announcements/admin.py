from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import Announcement

@admin.register(Announcement)
class AnnouncementAdmin(ModelAdmin):
    list_display = ('title', 'signed_by', 'release_at', 'expiry_at', 'is_active', 'priority')
    search_fields = ('title', 'description')
    list_filter = ('is_active', 'release_at', 'expiry_at')
    filter_horizontal = ('classrooms', 'subjects')

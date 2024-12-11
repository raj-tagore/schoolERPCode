from django.contrib import admin
from .models import Announcement

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'signed_by', 'release_date', 'expiry_date', 'is_active', 'priority')
    search_fields = ('title', 'description')
    list_filter = ('is_active', 'release_date', 'expiry_date')
    filter_horizontal = ('classrooms', 'subjects')

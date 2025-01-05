from django.contrib import admin
from .models import Announcement
from import_export.admin import ImportExportModelAdmin

@admin.register(Announcement)
class AnnouncementAdmin(ImportExportModelAdmin):
    list_display = ('title', 'signed_by', 'release_at', 'expiry_at', 'is_active', 'priority')
    search_fields = ('title', 'description')
    list_filter = ('is_active', 'release_at', 'expiry_at')
    filter_horizontal = ('classrooms', 'subjects')

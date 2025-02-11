from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Calendar, Event

@admin.register(Calendar)
class CalendarAdmin(ImportExportModelAdmin):
    list_display = ('name', 'is_school_wide', 'created_by')
    search_fields = ('name', 'description')
    filter_horizontal = ('classrooms', 'subjects', 'users')

@admin.register(Event)
class EventAdmin(ImportExportModelAdmin):
    list_display = ('title', 'calendar', 'start', 'end', 'created_by')
    search_fields = ('title',)
    list_filter = ('calendar', 'start', 'end')

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Event

@admin.register(Event)
class EventAdmin(ImportExportModelAdmin):
    list_display = ('title', 'start', 'end', 'created_by')
    search_fields = ('title',)
    list_filter = ('start', 'end')
    filter_horizontal = ('classrooms', 'subjects')
from django.contrib import admin
from .models import Assignment, SubmittedAssignment
from import_export.admin import ImportExportModelAdmin

@admin.register(Assignment)
class AssignmentAdmin(ImportExportModelAdmin):
    list_display = ('title', 'subject', 'release_at', 'due_at', 'is_active')
    search_fields = ('title', 'description')
    list_filter = ('is_active', 'release_at', 'due_at')

@admin.register(SubmittedAssignment)
class StudentAssignmentAdmin(ImportExportModelAdmin):
    list_display = ('student', 'assignment', 'status', 'submission_datetime')
    search_fields = ('student__user__username', 'assignment__title')
    list_filter = ('status',)

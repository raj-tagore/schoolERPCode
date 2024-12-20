from django.contrib import admin
from .models import Assignment, SubmittedAssignment

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'release_datetime', 'due_datetime', 'is_active')
    search_fields = ('title', 'description')
    list_filter = ('is_active', 'release_datetime', 'due_datetime')

@admin.register(SubmittedAssignment)
class StudentAssignmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'assignment', 'status', 'submission_datetime')
    search_fields = ('student__user__username', 'assignment__title')
    list_filter = ('status',)

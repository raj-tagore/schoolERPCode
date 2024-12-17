from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import Assessment, StudentAssessment

@admin.register(Assessment)
class AssessmentAdmin(ModelAdmin):
    list_display = ('title', 'subject', 'datetime', 'venue', 'is_active')
    search_fields = ('title', 'description', 'venue')
    list_filter = ('is_active', 'datetime', 'subject')

@admin.register(StudentAssessment)
class StudentAssessmentAdmin(ModelAdmin):
    list_display = ('student', 'assessment', 'marks', 'status')
    search_fields = ('student__user__username', 'assessment__title')
    list_filter = ('status',)

from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(ModelAdmin):
    list_display = ('student', 'date', 'subject', 'classroom', 'record')
    search_fields = ('student__user__username', 'subject__name', 'classroom__name')
    list_filter = ('date', 'subject', 'classroom', 'record')

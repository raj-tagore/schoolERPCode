from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('classroom', 'subject', 'date')
    search_fields = ('student__user__username', 'subject__name', 'classroom__name')
    list_filter = ('date', 'subject', 'classroom')

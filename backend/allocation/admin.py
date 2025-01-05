from django.contrib import admin
from .models import Classroom, Subject
from import_export.admin import ImportExportModelAdmin

@admin.register(Classroom)
class ClassroomAdmin(ImportExportModelAdmin):
    list_display = ("name", "standard", "is_active", "class_teacher")
    search_fields = ("name", "standard")
    list_filter = ("is_active",)
    filter_horizontal = ("students",)


@admin.register(Subject)
class SubjectAdmin(ImportExportModelAdmin):
    list_display = ("name", "classroom", "is_active", "teacher")
    search_fields = ("name", "description")
    list_filter = ("is_active", "classroom")

from django.contrib import admin
from .models import Classroom, Subject


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ("name", "standard", "is_active", "class_teacher")
    search_fields = ("name", "standard")
    list_filter = ("is_active",)
    filter_horizontal = ("students", "other_teachers")


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "classroom", "is_active", "main_teacher")
    search_fields = ("name", "description")
    list_filter = ("is_active", "classroom")
    filter_horizontal = ("other_teachers", "additional_students")

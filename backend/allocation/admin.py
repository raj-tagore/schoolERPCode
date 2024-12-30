from django.contrib import admin

from allocation.models.classroom import Classroom
from allocation.models.subject import Subject



@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ("name", "standard", "is_active", "class_teacher")
    search_fields = ("name", "standard")
    list_filter = ("is_active",)

    @admin.display(description='Student')
    def get_author_name(self, obj):
        return obj.students


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "classroom", "is_active", "main_teacher")
    search_fields = ("name", "description")
    list_filter = ("is_active", "classroom")
    filter_horizontal = ("other_teachers", "additional_students")


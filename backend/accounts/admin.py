from django.contrib import admin
from .models import Student, Teacher, Parent
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    pass

@admin.register(Teacher)
class TeacherAdmin(ImportExportModelAdmin):
    pass

@admin.register(Parent)
class ParentAdmin(ImportExportModelAdmin):
    pass

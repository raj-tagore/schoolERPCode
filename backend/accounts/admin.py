from django.contrib import admin
from .models import Student, Teacher, Parent

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    pass

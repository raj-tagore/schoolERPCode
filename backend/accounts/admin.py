from django.contrib import admin
from .models import Staff, Teacher, Student

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone', 'whatsapp', 'role', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'whatsapp', 'role')
    list_filter = ('is_active', 'role')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone', 'whatsapp', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'whatsapp')
    list_filter = ('is_active',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone', 'whatsapp', 'standard', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'whatsapp', 'standard')
    list_filter = ('is_active', 'standard')

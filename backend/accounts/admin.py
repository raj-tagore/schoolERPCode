from django.contrib import admin
from .models import Student, Teacher, Parent
from import_export.admin import ImportExportModelAdmin
from import_export import resources

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        fields = '__all__'

class TeacherResource(resources.ModelResource):
    class Meta:
        model = Teacher
        fields = '__all__'

class ParentResource(resources.ModelResource):
    class Meta:
        model = Parent
        fields = '__all__'

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

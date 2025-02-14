from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib.auth.hashers import make_password

class UserResource(resources.ModelResource):
    def before_save_instance(self, instance, row, **kwargs):
        if instance.password and not instance.password.startswith('pbkdf2_'):
            instance.password = make_password(instance.password)
        return super().before_save_instance(instance, row, **kwargs)
    
    def dehydrate_password(self, user):
        # Exclude or mask password during export
        return "*****"

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'school')

@admin.register(User)
class UsersAdmin(BaseUserAdmin, ImportExportModelAdmin):
    resource_class = UserResource
    list_display = ('email', 'first_name', 'last_name', 'school')
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'school')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'is_approved'),
        }),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'school'),
        }),
    )
    
    ordering = ('email',)
    search_fields = ('email', 'first_name', 'last_name')


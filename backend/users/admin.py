from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
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
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'school', 'groups')

@admin.register(User)
class UsersAdmin(UserAdmin, ImportExportModelAdmin):
    resource_class = UserResource
    list_display = ('username', 'first_name', 'last_name', 'school')
    
    # Fields for the Account detail view
    fieldsets = UserAdmin.fieldsets + (
        (_('Additional Information'), {
            'fields': ('is_approved', 'school'),
        }),
    )


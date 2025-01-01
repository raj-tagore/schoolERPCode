from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User
from import_export.admin import ImportExportModelAdmin

@admin.register(User)
class UsersAdmin(UserAdmin, ImportExportModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'school')
    
    # Fields for the Account detail view
    fieldsets = UserAdmin.fieldsets + (
        (_('Additional Information'), {
            'fields': ('is_approved',),
        }),
    )

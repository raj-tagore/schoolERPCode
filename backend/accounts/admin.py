from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Account

@admin.register(Account)
class AccountAdmin(BaseUserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('is_active', 'groups')  

    # Define the sections in the Account detail view
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal Information'), {
            'fields': ('first_name', 'last_name', 'email', 'address', 'phone', 'whatsapp', 'standard'),
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_approved', 'groups', 'user_permissions'),  
        }),
    )

    # Specify the fields for Account creation view in the admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'is_active', 'groups', 'user_permissions'),
        }),
    )

    ordering = ('username',)
    # Filter options based on custom groups and permissions
    filter_horizontal = ('groups', 'user_permissions')


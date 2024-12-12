from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Account

@admin.register(Account)
class AccountAdmin(UserAdmin):
    # Displayed in the list view
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('is_active', 'groups')  

    # Fields for the Account detail view
    fieldsets = UserAdmin.fieldsets + (
        (_('Additional Information'), {
            'fields': ('address', 'phone', 'whatsapp', 'standard', 'is_approved'),
        }),
    )

    # Fields for the Account creation view
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': ('address', 'phone', 'whatsapp', 'standard', 'is_approved'),
        }),
    )

    ordering = ('username',)

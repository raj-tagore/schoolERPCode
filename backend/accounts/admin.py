from unfold.admin import ModelAdmin
from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Account

@admin.register(Account)
class AccountAdmin(ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'school')
    
    # Fields for the Account detail view
    # fieldsets = UserAdmin.fieldsets + (
    #     (_('Additional Information'), {
    #         'fields': ('is_approved', 'address', 'school', 'phone', 'whatsapp'),
    #     }),
    # )

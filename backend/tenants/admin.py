from django.contrib import admin
from .models import School, Domain
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Displayed in the list view
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('is_active', 'groups')  

    ordering = ('username',)

# Register the School model
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on')  
    search_fields = ('name',)

# Register the Domain model
@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain', 'tenant')  
    search_fields = ('domain',)


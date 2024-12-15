from django.contrib import admin
from .models import School, Domain
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# Register the School model
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name',)  
    search_fields = ('name',)

# Register the Domain model
@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain', 'tenant')  
    search_fields = ('domain',)


from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import School, Domain
from unfold.admin import ModelAdmin
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# Register the School model
@admin.register(School)
class SchoolAdmin(ModelAdmin):
    list_display = ('name',)  
    search_fields = ('name',)

# Register the Domain model
@admin.register(Domain)
class DomainAdmin(ModelAdmin):
    list_display = ('domain', 'tenant')  
    search_fields = ('domain',)


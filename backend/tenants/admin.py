from django.contrib import admin
from .models import School, Domain

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


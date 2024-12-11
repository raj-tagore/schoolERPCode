from django.contrib import admin
from .models import Attachment

@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'file', 'is_active', 'created_at', 'updated_at')
    search_fields = ('file', 'name')
    list_filter = ('is_active', 'created_at', 'updated_at')

from django.db import models

# Create your models here.

class Attachment(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    file = models.FileField(upload_to='attachments/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    additional_info = models.TextField(null=True, blank=True)
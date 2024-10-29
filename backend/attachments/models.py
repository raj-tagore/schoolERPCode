from django.db import models

# Create your models here.

class Attachment(models.Model):
    file = models.FileField(upload_to='attachments/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Attachment for {self.content_object} uploaded at {self.uploaded_at}"

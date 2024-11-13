from django.db import models

# Create your models here.

class Announcement(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    signed_by = models.ForeignKey('accounts.Account', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    release_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    
    classrooms = models.ManyToManyField('allocation.Classroom', blank=True, related_name='attachments')
    subjects = models.ManyToManyField('allocation.Subject', blank=True, related_name='attachments')

    
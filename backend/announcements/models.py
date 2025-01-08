from django.db import models

# Create your models here.

class Announcement(models.Model):

    PRIORITY_CHOICES = [
        ('low', 'Low Priority'),
        ('medium', 'Medium Priority'),
        ('high', 'High  Priority')]

    title = models.CharField(max_length=50)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    is_school_wide = models.BooleanField(default=False)
    created_by = models.ForeignKey('accounts.Teacher', on_delete=models.SET_NULL, null=True, related_name='announcements_created')
    signed_by = models.ForeignKey('accounts.Teacher', on_delete=models.SET_NULL, null=True, related_name='announcements_signed')
    created_at = models.DateTimeField(auto_now_add=True)
    release_at = models.DateTimeField()
    expiry_at = models.DateTimeField()
    priority = models.CharField(max_length=10, blank=True, choices=PRIORITY_CHOICES, null=True)
    
    classrooms = models.ManyToManyField('allocation.Classroom', blank=True, related_name='announcements')
    subjects = models.ManyToManyField('allocation.Subject', blank=True, related_name='announcements')

    attachments = models.ManyToManyField('attachments.Attachment', blank=True, related_name='announcements')
    
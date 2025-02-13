from django.db import models
from allocation.models import Classroom, Subject
from attachments.models import Attachment
from accounts.models import Teacher

class Calendar(models.Model):
    name = models.TextField()
    description = models.TextField(null=True, blank=True)

    classrooms = models.ManyToManyField(Classroom, blank=True)
    subjects = models.ManyToManyField(Subject, blank=True)
    
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="calendars")
    is_school_wide = models.BooleanField(default=True)

class Event(models.Model):
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE, null=False, related_name="events")
    title = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    attachment = models.ForeignKey(Attachment, on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="events")


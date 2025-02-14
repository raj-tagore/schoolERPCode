from django.db import models
from allocation.models import Classroom, Subject
from attachments.models import Attachment
from accounts.models import Teacher

class Event(models.Model):
    title = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    classrooms = models.ManyToManyField(Classroom, blank=True)
    subjects = models.ManyToManyField(Subject, blank=True)
    is_school_wide = models.BooleanField(default=True)

    attachment = models.ForeignKey(Attachment, on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="events")


from django.db import models
from users.models import User
from attachments.models import Attachment


# Create your models here.
class Report(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    submission_deadline = models.DateTimeField()
    SUBMISSION_FREQUENCIES = [
        ("O", "One time"),
        ("D", "Daily"),
        ("W", "Weekly"),
        ("N", "Every N months"),
        ("M", "Monthly"),
        ("Y", "Yearly"),
    ]
    submission_frequency = models.CharField(choices=SUBMISSION_FREQUENCIES, max_length=1, default="O")
    is_active = models.BooleanField(default=True)
    attachment = models.ForeignKey(Attachment, on_delete=models.SET_NULL, null=True, blank=True)

class SubmittedReport(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    attachment = models.ForeignKey(Attachment, on_delete=models.SET_NULL, null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    approved_at = models.DateTimeField(null=True, blank=True)

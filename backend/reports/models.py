from django.db import models
from users.models import User
from attachments.models import Attachment
from allocation.models import Classroom


# Create your models here.
class ReportMeta(models.Model):
    REPORT_TYPES = [
        ("FE", "Fee Report"),
        ("AT", "Attendance Report")
    ]
    report_type = models.CharField(max_length=2, choices=REPORT_TYPES)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    attachment = models.ForeignKey(Attachment, on_delete=models.SET_NULL, null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    approved_at = models.DateTimeField(null=True, blank=True)

class AttendanceReport:
    metadata = models.ForeignKey(ReportMeta, on_delete=models.CASCADE, null=False, related_name="attendance_report")
    date = models.DateField(null=False)
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, related_name='report')
    remarks = models.TextField()

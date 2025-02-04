from django.db import models
from attachments.models import Attachment


class Event(models.Model):
    title = models.TextField()
    description = models.TextField()
    attachment = models.ForeignKey(Attachment, on_delete=models.SET_NULL)
    date = models.DateField(null=False)

    REPEAT_PERIOD_CHOICES = [("W", "Weekly"), ("M", "Monthly"), ("Y", "Yearly")]
    repeat_period = models.CharField(choices=REPEAT_PERIOD_CHOICES, null=False)

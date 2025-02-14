from django.db import models

from allocation.models import Subject

# Create your models here.


class Period(models.Model):
    start = models.TimeField(null=False)
    end = models.TimeField(null=False)
    CHOICES = [
        ("MO", "Monday"),
        ("TU", "Tuesday"),
        ("WE", "Wednesday"),
        ("TH", "Thursday"),
        ("FR", "Friday"),
        ("SA", "Saturday"),
        ("SU", "Sunday"),
    ]
    day = models.CharField(null=False, choices=CHOICES)


class TimeTable(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    periods = models.ManyToManyField(Period)

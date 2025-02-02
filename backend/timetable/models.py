from django.db import models

from allocation.models import Subject

# Create your models here.

class Period(models.Model):
    start = models.TimeField(null=False)
    end = models.TimeField(null=False)
    choices = [
        (0, "Monday"),
        (1, "Tuesday"),
        (2, "Wednesday"),
        (3, "Thursday"),
        (4, "Friday"),
        (5, "Saturday"),
        (6, "Sunday"),
    ]
    day = models.IntegerChoices(null=False, choices=choices)


class TimeTable(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=False)
    periods = models.ManyToManyField(Period, on_delete=models.CASCADE, null=False)

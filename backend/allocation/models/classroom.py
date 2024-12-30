from typing import final

from django.db import models

from accounts.models import Account


@final
class Classroom(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    standard = models.CharField(max_length=50)
    class_teacher = models.ForeignKey(
        Account,
        on_delete=models.SET_NULL,
        null=True,
        related_name="classrooms_leading",
        limit_choices_to={"groups__name": "Teacher"},
    )
    other_teachers = models.ManyToManyField(
        Account,
        related_name="classrooms_assisting",
        limit_choices_to={"groups__name": "Teacher"},
        blank=True,
    )

    def __str__(self):
        return self.name

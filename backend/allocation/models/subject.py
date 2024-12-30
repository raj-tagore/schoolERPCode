from typing import final

from django.db import models

from accounts.models import Account
from allocation.models.classroom import Classroom


@final
class Subject(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    classroom = models.ForeignKey(
        Classroom, on_delete=models.SET_NULL, null=True, related_name="subjects"
    )
    main_teacher = models.ForeignKey(
        Account,
        on_delete=models.SET_NULL,
        null=True,
        related_name="subjects_leading",
        limit_choices_to={"groups__name": "Teacher"},
    )
    other_teachers = models.ManyToManyField(
        Account,
        related_name="subjects_assisting",
        limit_choices_to={"groups__name": "Teacher"},
        blank=True,
    )
    additional_students = models.ManyToManyField(
        Account,
        related_name="subjects",
        limit_choices_to={"groups__name": "Student"},
        blank=True,
    )

    def __str__(self):
        return self.name

from typing import final

from django.db import models

from allocation.models.classroom import Classroom
from allocation.models.student import Student


@final
class ReportCard(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="report_cards", null=False
    )

    classroom = models.ForeignKey(
        Classroom, on_delete=models.CASCADE, related_name="report_cards", null=False
    )

    marks = models.DecimalField("Marks", max_digits=5, decimal_places=2, null=False)

    grade = models.CharField("Grade", max_length=2, null=False)

    remarks = models.TextField("Remarks", blank=True)

    file = models.FileField("File", upload_to="report_cards")

    def __str__(self):
        return f"{self.student.account.username} - {self.subject.name}"

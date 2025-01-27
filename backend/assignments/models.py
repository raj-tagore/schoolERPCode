from django.db import models


# Create your models here.
class Assignment(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    release_datetime = models.DateTimeField()
    due_datetime = models.DateTimeField()
    subject = models.ForeignKey(
        "allocation.Subject",
        on_delete=models.CASCADE,
        null=False,
        related_name="assignments",
    )

    def __str__(self):
        return self.title


class SubmittedAssignment(models.Model):
    student = models.ForeignKey(
        'accounts.Student',
        on_delete=models.CASCADE,
        related_name="student",
        null=False,
        blank=True,
    )
    assignment = models.ForeignKey(
        Assignment,
        on_delete=models.CASCADE,
        related_name="assignment",
        null=False,
        blank=True,
    )
    status = models.CharField(max_length=50, null=False)
    submission_datetime = models.DateTimeField(null=False, blank=True)

    def __str__(self):
        return self.assignment.title + " - " + self.student.username

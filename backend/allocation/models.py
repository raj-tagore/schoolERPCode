import uuid
from django.db import models
from accounts.models import Student, Teacher

# Create your models here.

class Classroom(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    standard = models.CharField(max_length=50)
    students = models.ManyToManyField(
        Student,
        related_name="classrooms",
        blank=True,
    )
    class_teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        related_name="classrooms_leading",
    )
    other_teachers = models.ManyToManyField(
        Teacher,
        related_name="classrooms_assisting",
        blank=True,
    )

    join_code = models.UUIDField(unique=True, default=uuid.uuid4, null=False)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    classroom = models.ForeignKey(
        Classroom, on_delete=models.SET_NULL, null=True, related_name="subjects"
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        related_name="subjects",
    )

    def __str__(self):
        return self.name + ' (' + self.classroom.name + ')'

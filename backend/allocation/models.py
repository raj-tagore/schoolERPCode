from django.db import models
from users.models import User

# Create your models here.


class Classroom(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    standard = models.CharField(max_length=50)
    students = models.ManyToManyField(
        User,
        related_name="classrooms",
        limit_choices_to={"groups__name": "Student"},
        blank=True,
    )
    class_teacher = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="classrooms_leading",
        limit_choices_to={"groups__name": "Teacher"},
    )
    other_teachers = models.ManyToManyField(
        User,
        related_name="classrooms_assisting",
        limit_choices_to={"groups__name": "Teacher"},
        blank=True,
    )

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    classroom = models.ForeignKey(
        Classroom, on_delete=models.SET_NULL, null=True, related_name="subjects"
    )
    main_teacher = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="subjects_leading",
        limit_choices_to={"groups__name": "Teacher"},
    )
    other_teachers = models.ManyToManyField(
        User,
        related_name="subjects_assisting",
        limit_choices_to={"groups__name": "Teacher"},
        blank=True,
    )
    additional_students = models.ManyToManyField(
        User,
        related_name="subjects",
        limit_choices_to={"groups__name": "Student"},
        blank=True,
    )

    def __str__(self):
        return self.name

class ClassroomJoinLinks(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='classroom_join_links')
    created_on = models.DateTimeField(auto_now_add=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='join_links')
    uuid = models.UUIDField(unique=True, editable=False, primary_key=True)

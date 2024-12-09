from django.db import models
from accounts.models import Account

# Create your models here.

class Classroom(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    standard = models.CharField(max_length=50)
    students = models.ManyToManyField(Account, related_name='classrooms', limit_choices_to={'group': 'Student'})
    class_teacher = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='classrooms_leading', limit_choices_to={'group': 'Teacher'})
    other_teachers = models.ManyToManyField(Account, related_name='classrooms_assisting', limit_choices_to={'group': 'Student'})

    def __str__(self):
        return self.name
    
class Subject(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, related_name='subjects')
    main_teacher = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='subjects_leading')
    other_teachers = models.ManyToManyField(Account, related_name='subjects_assisting')
    additional_students = models.ManyToManyField(Account, related_name='subjects')
    
    def __str__(self):
        return self.name

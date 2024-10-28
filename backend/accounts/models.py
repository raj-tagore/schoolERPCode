from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    standard = models.CharField(max_length=50)
    """
    classroom
    subjects
    """

    def __str__(self):
        return self.username

class Staff(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    """
    classrooms
    subjects
    """

    def __str__(self):
        return self.username
    
class Classroom(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    standard = models.CharField(max_length=50)
    
    """
    staff
    students
    subjects
    """

    def __str__(self):
        return self.name

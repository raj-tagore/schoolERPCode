from django.db import models
from django.contrib.auth.models import Group
from users.models import User
from django.db.models import Q

def get_parent_group():
    return Group.objects.get_or_create(name='Parent')[0].id

def get_teacher_group():
    return Group.objects.get_or_create(name='Teacher')[0].id

def get_student_group():
    return Group.objects.get_or_create(name='Student')[0].id

# Create your models here.
class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='parent_account')
    group = models.ForeignKey(Group, on_delete=models.PROTECT, default=get_parent_group)
    phone = models.CharField('Phone number', max_length=20, blank=True)
    whatsapp = models.CharField('WhatsApp number', max_length=20, blank=True)

    @property
    def children(self):
        return Student.objects.filter(
            Q(guardian_1=self) | Q(guardian_2=self)
        ).distinct()

    def __str__(self):
        return f"{self.user.full_name} ({self.user.email})"

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_account')
    group = models.ForeignKey(Group, on_delete=models.PROTECT, default=get_teacher_group)
    identifier = models.BigIntegerField('ID')
    phone = models.CharField('Phone number', max_length=20, blank=True)
    whatsapp = models.CharField('WhatsApp number', max_length=20, blank=True)

    class Meta:
        ordering = ['identifier']

    def __str__(self):
        return f"{self.user.full_name} ({self.user.email})"

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_account')
    group = models.ForeignKey(Group, on_delete=models.PROTECT, default=get_student_group)
    
    # Basic Fields
    student_no = models.CharField(max_length=50, unique=True)
    roll_no = models.CharField(max_length=50, blank=True, null=True)
    
    # Guardians
    guardian_1 = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True, blank=True, related_name='student_guardian1')
    guardian_2 = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True, blank=True, related_name='student_guardian2')


    class Meta:
        ordering = ['student_no']

    def __str__(self):
        return f"{self.user.full_name} ({self.user.email})"


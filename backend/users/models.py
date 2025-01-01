from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from tenants.models import School

class User(AbstractUser):

    is_approved = models.BooleanField(default=False) 

    groups = models.ManyToManyField(Group, related_name="users", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="users", blank=True)

    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='users', null=True)

    def __str__(self):
        return self.username

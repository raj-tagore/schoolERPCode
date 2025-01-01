from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from tenants.models import School

class Account(AbstractUser):

    is_approved = models.BooleanField(default=False) 

    groups = models.ManyToManyField(Group, related_name="accounts", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="accounts", blank=True)

    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='accounts', null=True)

    def __str__(self):
        return self.username




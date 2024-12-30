from typing import final
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from tenants.models import School


@final
class Account(AbstractUser):
    address = models.CharField("Address", max_length=1000, blank=False)
    phone = models.CharField("Phone number", max_length=20, blank=False)
    whatsapp = models.CharField("WhatsApp number", max_length=20, blank=False)

    dob = models.DateField("Date of birth", null=False)

    is_approved = models.BooleanField(default=False)

    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="teachers", null=True,
    )

    groups = models.ManyToManyField(Group, related_name="accounts", blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name="accounts", blank=True
    )

    def __str__(self):
        return self.username



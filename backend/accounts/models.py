from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from guardian.mixins import GuardianUserMixin

class Account(AbstractUser, GuardianUserMixin):
    address = models.CharField('Address', max_length=1000, blank=True)
    phone = models.CharField('Phone number', max_length=20, blank=True)
    whatsapp = models.CharField('WhatsApp number', max_length=20, blank=True)

    is_approved = models.BooleanField(default=False) 
    standard = models.IntegerField(null=True, blank=True) 

    groups = models.ManyToManyField(Group, related_name="accounts", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="accounts", blank=True)

    def __str__(self):
        return self.username
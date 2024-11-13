# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Permission, Group
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

class AccountManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError(_('The Username must be set'))
        user = self.model(username=username, **extra_fields)
        user.set_password(password)  # Hashes the password
        user.save()
        return user

class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('Username'), max_length=100, unique=True)
    first_name = models.CharField(_('First Name'), max_length=100)
    last_name = models.CharField(_('Last Name'), max_length=100)
    is_active = models.BooleanField(_('Active'), default=True)
    email = models.EmailField(_('Email'), blank=True)
    address = models.CharField(_('Address'), max_length=1000)
    phone = PhoneNumberField(_('Phone number'), blank=True)
    whatsapp = PhoneNumberField(_('WhatsApp number'), blank=True)
    
    is_approved = models.BooleanField(default=False) # For teachers
    standard = models.IntegerField(null=True) # For students
    
    groups = models.ManyToManyField(
        Group,
        related_name="accounts",  
        blank=True,
        help_text="The groups this user belongs to.",
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="accounts",  
        blank=True,
        help_text="Specific permissions for this user.",
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'email']

    objects = AccountManager()

    def __str__(self):
        return self.username


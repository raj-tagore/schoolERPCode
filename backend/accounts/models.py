# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Permission, Group
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _mod

class AccountManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError(_('The Username must be set'))
        user = self.model(username=username, **extra_fields)
        user.set_password(password)  # Hashes the password
        user.save()
        return user

class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Username', max_length=100, unique=True)
    first_name = models.CharField('First Name', max_length=100, blank=True)
    last_name = models.CharField('Last Name', max_length=100, blank=True)
    is_active = models.BooleanField('Active', default=True)
    email = models.EmailField('Email', blank=True)
    address = models.CharField('Address', max_length=1000, blank=True)
    phone = PhoneNumberField('Phone number', blank=True)
    whatsapp = PhoneNumberField('WhatsApp number', blank=True)
    
    is_approved = models.BooleanField(default=False) # For teachers
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='Designates whether the user is a staff member.',
    )
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


    objects = AccountManager()

    def __str__(self):
        return self.username
    
    # Implement the methods required for permissions
    def has_perm(self, perm, obj=None):
        """
        Returns True if the account has the specified permission.
        """
        if self.is_active and self.is_superuser:
            return True

        # Split the permission string if it contains an app label
        if '.' in perm:
            app_label, codename = perm.split('.', 1)
        else:
            codename = perm

        # Check user permissions
        if self.user_permissions.filter(codename=codename).exists():
            return True

        # Check group permissions
        if self.groups.filter(permissions__codename=codename).exists():
            return True

        return False

    def has_perms(self, perm_list, obj=None):
        """
        Returns True if the account has all permissions in the list.
        """
        return all(self.has_perm(perm, obj) for perm in perm_list)

    def get_all_permissions(self, obj=None):
        """
        Returns a set of permission strings the account has.
        """
        if not self.is_active:
            return set()

        if self.is_superuser:
            permissions = Permission.objects.all()
        else:
            permissions = self.user_permissions.all() | Permission.objects.filter(group__account_groups__account=self)

        return set(f"{perm.content_type.app_label}.{perm.codename}" for perm in permissions)

    def get_group_permissions(self, obj=None):
        """
        Returns a set of permission strings the account has via its groups.
        """
        if not self.is_active:
            return set()

        permissions = Permission.objects.filter(group__account_groups__account=self)
        return set(f"{perm.content_type.app_label}.{perm.codename}" for perm in permissions)


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from tenants.models import School

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="users", null=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    @property
    def account(self):
        if hasattr(self, "teacher_account"):
            return {"type": "Teacher", "id": self.teacher_account.id}
        if hasattr(self, "parent_account"):
            return {"type": "Parent", "id": self.parent_account.id}
        if hasattr(self, "student_account"):
            return {"type": "Student", "id": self.student_account.id}
        return None

    @property
    def full_name(self):
        return " ".join([self.first_name, self.last_name])

    def __str__(self):
        return self.username

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from tenants.models import School


class User(AbstractUser):
    is_approved = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, related_name="users", blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name="users", blank=True
    )

    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="users", null=True
    )

    @property
    def permissions(self):
        return list(self.get_all_permissions())

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

from typing import final
from rest_framework.permissions import BasePermission

from accounts.models import Account

@final
class AccountPermissions(BasePermission):

    def has_object_permission(self, request, view, obj: Account):

        if request.user.is_superuser:
            return True

        if obj == request.user:
            return True

        if "Admin" in [group.name for group in request.user.groups.all()]:
            # Admins cannot manage superusers
            if obj.is_superuser:
                return False
            return True

        if "Teacher" in [group.name for group in request.user.groups.all()]:
            # Teachers can manage students if they share at least one classroom
            if "Student" in [group.name for group in obj.groups.all()]:
                common_classrooms = request.user.classrooms.filter(id__in=obj.classrooms.values_list('id', flat=True))
                return common_classrooms.exists()
            return False

        return False
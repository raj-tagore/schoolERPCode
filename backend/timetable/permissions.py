from rest_framework.permissions import BasePermission


class PeriodPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if "Admin" in [group.name for group in request.user.groups.all()]:
            return True

        # Check if user is in the 'Teacher' group
        if "Teacher" in [group.name for group in request.user.groups.all()]:
            # Check if user is teaching or assisting in any related classroom
            return True
        return False


class TimeTablePermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if "Admin" in [group.name for group in request.user.groups.all()]:
            return True

        # Check if user is in the 'Teacher' group
        if "Teacher" in [group.name for group in request.user.groups.all()]:
            # Check if user is teaching or assisting in any related classroom
            return True

        return False

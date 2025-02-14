from rest_framework.permissions import BasePermission, SAFE_METHODS

class ReportPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if "Admin" in [group.name for group in request.user.groups.all()]:
            return True

        # Check if user is in the 'Teacher' group
        if "Teacher" in [group.name for group in request.user.groups.all()]:
            # Check if user is teaching or assisting in any related classroom
            return True
        if "Student" in [group.name for group in request.user.groups.all()]:
            if request.method in SAFE_METHODS:
                return True
        return False

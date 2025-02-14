from rest_framework.permissions import BasePermission
from schoolERPCode.viewsets import ALL_PERMISSIONS


class UserPermissions(BasePermission):
    # Used for returning permissions to the frontend
    def get_permissions(request, obj):
        if request.user.is_superuser:
            return ALL_PERMISSIONS

        if obj == request.user:
            return ALL_PERMISSIONS

        if "Admin" in [group.name for group in request.user.groups.all()]:
            # Admins cannot manage superusers
            if obj.is_superuser or "Admin" in [
                group.name for group in obj.groups.all()
            ]:
                return ["GET"]

        if "Teacher" in [group.name for group in request.user.groups.all()]:
            # Teachers can manage students if they share at least one classroom
            if "Student" in [group.name for group in obj.groups.all()]:
                common_classrooms = request.user.classrooms.filter(
                    id__in=obj.classrooms.values_list("id", flat=True)
                )
                if common_classrooms.exists():
                    return ALL_PERMISSIONS
            return ["GET"]

        return ["GET"]
    
    # Used internally for actually checking permissions
    def has_object_permission(self, request, view, obj):
        if request.method in self.__class__.get_permissions(request, obj):
            return True

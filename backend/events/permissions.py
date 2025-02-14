from rest_framework.permissions import BasePermission
from schoolERPCode.viewsets import ALL_PERMISSIONS


class EventPermissions(BasePermission):
    def get_permissions(request, obj):
        if request.user.is_superuser:
            return ALL_PERMISSIONS
        if request.user.id in obj.created_by:
            return ["GET", "DELETE", "PATCH"]
        if request.user.id in obj.calendar.users:
            return ["GET"]
        return []
        
    def has_object_permission(self, request, view, obj):
        if request.method in self.__class__.get_permissions(request, obj):
            return True

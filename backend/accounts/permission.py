import rest_framework.permissions import BasePermissions

class AccountViewSetPermissions(BasePermissions):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user or request.user.is_staff

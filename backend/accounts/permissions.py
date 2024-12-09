import rest_framework.permissions import BasePermissions

class AccountViewSetPermissions(BasePermissions):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET']:
            return True
        return request.user.username == obj.username && request.is_staff && request.user.is_approved

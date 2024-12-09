import rest_framework.permissions import BasePermissions

class AccountViewSetPermissions(BasePermissions):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'POST']:
            return request.is_staff
        return request.user.username == obj.username

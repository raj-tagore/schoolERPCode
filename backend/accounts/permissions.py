from rest_framework.permissions import BasePermission

class AccountObjectPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user

        # If Admin or is_staff
        if user.groups.filter(name='Admin').exists() or request.user.is_staff:
            return True

        # If Staff
        if user.groups.filter(name='Staff').exists() and not obj.groups.filter(name='Admin').exists():
            return True

        if user.groups.filter(name='Teacher').exists():
            # Is Teacher
            leading_classes = user.classrooms_leading.all()
            assisting_classes = user.classrooms_assisting.all()
            obj_classes = obj.classrooms.all()
            
            return (
                leading_classes.intersection(obj_classes).exists()
                or assisting_classes.intersection(obj_classes).exists()
            )

        # Not teacher
        return user.username == obj.username


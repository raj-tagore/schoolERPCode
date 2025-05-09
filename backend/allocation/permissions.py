from rest_framework.permissions import BasePermission, SAFE_METHODS


class ClassroomPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if "Admin" in [group.name for group in request.user.groups.all()]:
            return True

        # Check if user is in the 'Teacher' group
        if "Teacher" in [group.name for group in request.user.groups.all()]:
            # Check if user is teaching or assisting in any related classroom
            if (
                obj.class_teacher == request.user
                or obj.other_teachers.filter(id=request.user.id).exists()
            ):
                return True
            if (
                obj.students.filter(id=request.user.id).exists()
                and request.method in SAFE_METHODS
            ):
                return True
        return False


class SubjectPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if "Admin" in [group.name for group in request.user.groups.all()]:
            return True

        # Check if user is in the 'Teacher' group
        if "Teacher" in [group.name for group in request.user.groups.all()]:
            # Check if user is teaching or assisting in any related classroom
            classrooms = obj.classrooms.all()
            if (
                classrooms.filter(class_teacher=request.user).exists()
                or classrooms.filter(other_teachers=request.user).exists()
            ):
                return True

            if (
                obj.students.filter(id=request.user.id).exists()
                and request.method in SAFE_METHODS
            ):
                return True
            return False

        return False

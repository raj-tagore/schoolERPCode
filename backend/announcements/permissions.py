from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group

class AnnouncementPermissions(BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser:
                return True
        
        if "Admin" in [group.name for group in request.user.groups.all()]:
            return True
        
        # Check if user is in the 'Teacher' group
        if "Teacher" in [group.name for group in request.user.groups.all()]:
            # Check if user is teaching or assisting in any related classroom
            classrooms = obj.classrooms.all()
            if classrooms.filter(class_teacher=request.user).exists() or \
               classrooms.filter(other_teachers=request.user).exists():
                return True

            # Check if user is teaching or assisting in any related subject
            subjects = obj.subjects.all()
            if subjects.filter(main_teacher=request.user).exists() or \
               subjects.filter(other_teachers=request.user).exists():
                return True
            return False
        
        return False
    
from rest_framework.permissions import DjangoModelPermissions

class AccountViewSetPermissions(DjangoModelPermissions):
    def has_object_permission(self, request, view, obj):
        print("Checking Permissions")
        user = request.user

        if user.groups.filter(name='Admin').exists() or user.is_staff:
            return True
        print("Not Admin")

        if user.groups.filter(name='Staff').exists() and not obj.groups.filter(name='Admin').exists():
            return True
        print("Not Staff")

        if user.groups.filter(name='Teacher').exists():
            print("Is Teacher")
            leading_classes = user.classrooms_leading.all()
            assisting_classes = user.classrooms_assisting.all()
            obj_classes = obj.classrooms.all()
            
            return (
                leading_classes.intersection(obj_classes).exists()
                or assisting_classes.intersection(obj_classes).exists()
            )

        print("Not Teacher")
        return user.username == obj.username


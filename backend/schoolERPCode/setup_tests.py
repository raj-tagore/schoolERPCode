from django.contrib.auth.models import Group

from users.models import User

def create_test_superuser():
    return User.objects.create_superuser("test_superuser", "test_superuser@test_email.com", "test_password")


def create_test_admin():
    user = User.objects.create_user("test_admin", "test_admin@test_email.com", "test_password")
    group = Group.objects.create(id=1, name="Admin")
    user.groups.add(group)
    user.save()
    group.save()
    return user

def create_test_teacher():
    user = User.objects.create_user("test_teacher", "test_teacher@test_email.com", "test_password")
    group = Group.objects.create(id=2, name="Teacher")
    user.groups.add(group)
    user.save()
    group.save()
    return user

def create_test_student():
    user = User.objects.create_user("test_student", "test_student@test_email.com", "test_password")
    group = Group.objects.create(id=3, name="Student")
    user.groups.add(group)
    user.save()
    group.save()
    return user

def create_test_parent():
    user = User.objects.create_user("test_parent", "test_parent@test_email.com", "test_password")
    group = Group.objects.create(id=4, name="Student")
    user.groups.add(group)
    user.save()
    group.save()
    return user



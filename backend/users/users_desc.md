# Users

All users, permissions and authentication happens in this app. This is on the shared tenant.

## Models

### User:
This holds the basic info required by a django user. Fields obtained when extended by `UserProfile` are:
```
username*, first_name, last_name, email, password, is_staff, is_active, is_superuser
groups, user_permissions
last_login, date_joined
```
Fields marked by '*' are mandatory. 

Now, this will also hold have a OneToOne relationship with multiple models like:

* Staff, Student, Parent/Guardian
* Other possible User Types like bus-driver (future)

---



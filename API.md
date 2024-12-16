# Accounts - /api/accounts/

```
id, fname, lname, dob, address,
phone_no, whatsapp, email,
username, password, school,
created_at, updated_at
groups, is_active, is_staff, is_superuser 
```

### /all
GET (filtered)

### /id
CRUD (permissions)

### /self
CRUD

### /create
Account creation

### /api/token
POST -> login:
request: {username, password}
response: {access, refresh}

### /api/token/refresh
POST
request: {refresh}
response: {access}

## Announcements

```
id, title, description, attachments,
created_by, signed_by, created_at, updated_at, is_active
release_datetime, expiry_datetime, priority,
classrooms, subjects, additional_students, user_permissions
```

### /api/announcements/all
GET (filtered)

### /api/announcements/id
CRUD

# Allocation - /api/allocation/

## Classrooms - /classrooms

### /all
GET (filtered) (limited info)

### /id
CRUD (permissions)

### /create

## Subjects - /subjects

Same as above

# Assessments

Same as above

# Assignments

Same as above
# API Reference

## Accounts

```
id, fname, lname, dob, address,
phone_no, whatsapp, email,
username, password, school,
created_at, updated_at
groups, is_active, is_staff, is_superuser 
```

### /api/accounts/all
GET -> get all accounts
filters applicable

### /api/accounts/id
GET ->  get account details
POST -> create
PATCH/PUT -> update
DELETE -> delete

### /api/accounts/self
GET -> self info
PUT/PATCH, DELETE

### /api/accounts/read
unrestricted access for all users
GET -> basic acc info

### /api/token
POST -> login:
request: username, password
response: access, refresh

### /api/token/refresh
POST
request: refresh
response: access

## Announcements

```
id, title, description, attachments,
created_by, signed_by, created_at, updated_at, is_active
release_datetime, expiry_datetime, priority,
classrooms, subjects, additional_students, user_permissions
```

### /api/announcements/all
GET -> get all announcements
filters applicable

### /api/announcements/id
GET, POST, PATCH/PUT, DELETE
# Accounts

All users, their roles, permissions, authentication, and data to be stored in this app 

## Models

### Account:
This holds the basic info required by a django user. Fields obtained when extended by `UserProfile` are:
```
username*, first_name, last_name, email, password, is_staff, is_active, is_superuser
groups*, user_permissions
last_login, date_joined
```
Fields marked by '*' are mandatory. Every user must be assigned a group on creation.
Other fields added by us are:
```
address, dob, is_approved, school
```

Now, this will also hold have a OneToOne relationship with multiple models like:

* Teacher, Student, Staff, Parent/Guardian
* Other possible User Types like bus-driver

### Teacher
This will have a OneToOne relationship with Account. 
* Only allow accounts with `group=Teacher` to pair with this model.
* These models are only for data-holding purposes, permission checks will only happen through the `group` field in the account model. 

Fields are:
```
phone_no, whatsapp,
identifier (similar to student_no)
qualifications
identity_proof (type, document), TET certificate, character_certificate, id_card
```
* Any documents will hold PrimaryKey relationships with the `Attachment` model.

### Student
Same conditions as Teacher

Fields are:
```
student_no, roll_no, standard, division, 

address, aadhar_card_no, previous_school_student_id, religion, birth_place, mother_tongue, nationality, caste_status, medical_info

prev_school_details: {
    name, address, udise_no, board
}

guardian_1, guardian_2

address_proof, birth_certificate, identity_proof,
character_certificate, id_card, leaving_certificate
report_cards
```
* `guardian_1` and `guardian_2` will be PrimaryKey relationships with `Account`.

Student creation will proceed in frontend as follows:
1. first page of form will be the basic details for creating an `Account`. Then a POST request will be sent to create the account. Upon successful creation, the account instance would be returned and we move on to second page
2. second page will be additional details of Student, Here a `Student` instance would be created and matched with the `Account`. Successful response moves us to the next page.
3. third page will be details of guardians. `Parent` instances would be created

API must be coded with the above in mind.

### Parent
Fields:
```
phone_no, whatsapp,
occupation, office_address (if applicable)
qualifications, annual_income,
```
* `Parent` instance, if generated programmatically, will not have a password. If any user tries to login, but the password does not exist, we must identify this and give the option to set a password. 
---



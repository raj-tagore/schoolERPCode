import csv
import datetime
import random
from django.contrib.auth.hashers import BCryptSHA256PasswordHasher

import os

dir_path = os.path.dirname(os.path.realpath(__file__))


lorem = "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat."

# Prinicpal, Vice Principal, admin wale teachers abhi nahi kar rahe add, because abhi uske liye kuch kaam nahi hai
classrooms_len = 50


teachers_per_subject = 3
parents_len = 50
students_per_classroom = 50
announcements_per_subject = 5
announcements_per_classroom = 5
announcements_per_school = 10
assignment_per_subject = 10

standards = 10
sections = 5

user_id = 2

data = {
    "user": [],
    "classroom": [],
    "teacher": [],
    "parent": [],
    "student": [],
    "subject": [],
    "announcement": [],
    "assignment": [],
}

subject_teachers = {
    "Math": [],
    "Science": [],
    "English": [],
    "PT": [],
    "Social Studies": [],
}

hasher = BCryptSHA256PasswordHasher()
password = hasher.encode("Pass1234#", hasher.salt())

def add_user(
    username: str, email: str, first_name: str, last_name: str, groups: int
) -> int:
    user_id = len(data["user"]) + 1
    data["user"].append(
        {
            "id": user_id,
            "username": username,
            "email": email,
            "password": password,
            "first_name": first_name,
            "last_name": last_name,
            "school": 2,
            "groups": groups,
        }
    )
    return user_id


def add_teacher(teacher_num: int, subject: str) -> int:
    teacher_id = len(data["teacher"]) + 1
    user_id = add_user(
        "Teacher {} for {}".format(teacher_num, subject),
        "teacher{}for{}@testerp.shouldnotexist.com".format(teacher_num, subject),
        "Teacher {}".format(teacher_num),
        "For {}".format(subject),
        2,
    )
    teacher = {
        "id": teacher_id,
        "user": user_id,
        "identifier": teacher_id + 69420,
        "phone": 8456123568 + user_id,
        "whatsapp": 9885456523 + user_id,
    }
    subject_teachers[subject].append(teacher)
    data["teacher"].append(teacher)
    return user_id


for subject in subject_teachers.keys():
    for teacher_num in range(teachers_per_subject):
        add_teacher(teacher_num, subject)


def add_guardian(student_id: int, guardian_num: int) -> int:
    user_id = add_user(
        "Guardian {} for {}".format(guardian_num, student_id),
        "guardian{}for{}".format(guardian_num, student_id),
        "Guardian {}".format(guardian_num),
        "For {}".format(student_id),
        4,
    )
    guardian_id = len(data["parent"]) + 1
    data["parent"].append(
        {
            "id": guardian_id,
            "user": user_id,
            "identifier": 621 + guardian_id,
            "phone": 9898989898 + guardian_id,
            "whatsapp": 9898989898 + guardian_id,
        }
    )
    return guardian_id


def add_student(student_num: int, standard: int, section: int) -> int:
    student_id = len(data["student"]) + 1
    user_id = add_user(
        "Student {} of Class {}-{}".format(
            student_num + 1, standard_idx + 1, chr((ord("A") + section_idx))
        ),
        "student{}of_class{}{}@testerp.shouldnotexist.com".format(
            student_num + 1, standard_idx + 1, chr((ord("A") + section_idx))
        ),
        "Student {}".format(student_num + 1),
        "For {}-{}".format(standard_idx + 1, chr((ord("A") + section_idx))),
        3,
    )
    data["student"].append(
        {
            "id": student_id,
            "user": user_id,
            "student_no": 621 + student_id,
            "roll_no": 42 + student_id,
            "guardian_1": add_guardian(student_id, 1),
            "guardian_2": add_guardian(student_id, 2),
        }
    )
    return student_id


def add_classroom(standard: int, section: int) -> int:
    classroom_id = len(data["classroom"]) + 1

    teachers = []
    for t in subject_teachers.values():
        teachers.append(random.choice(t)["id"])

    for subject_name, s_teachers in subject_teachers.items():
        teacher = None
        for s_teacher in map(lambda t: t["id"], s_teachers):
            if s_teacher in teachers:
                teacher = s_teacher
                break
        data["subject"].append(
            {
                "id": len(data["subject"]) + 1,
                "name": subject_name,
                "is_active": len(data["subject"]) % 2 == 0,
                "description": "Subject {} of Classroom {}{}".format(
                    subject_name, standard_idx + 1, chr((ord("A") + section_idx))
                ),
                "classroom": classroom_id,
                "teacher": teacher,
            }
        )

    class_teacher = teachers.pop()

    students = []

    for student_idx in range(random.randint(40, 45)):
        students.append(add_student(student_idx, standard, section))

    data["classroom"].append(
        {
            "id": classroom_id,
            "name": "Class {standard}-{section}".format(
                standard=standard + 1, section=chr((ord("A") + section))
            ),
            "is_active": classroom_id % 2 == 0,
            "standard": standard + 1,
            "students": students,
            "class_teacher": class_teacher,
            "other_teachers": teachers,
        }
    )
    return classroom_id


for standard_idx in range(standards):
    for section_idx in range(sections):
        _ = add_classroom(standard_idx, section_idx)


for subject_idx, subject in enumerate(data["subject"]):
    for i in range(assignment_per_subject):
        data["assignment"].append(
            {
                "title": "Assignment {} for {}".format(i + 1, subject["name"]),
                "description": "Assignment description for assignment id {} for Subject: {}".format(
                    i + 1, subject["description"]
                ),
                "is_active": i % 2 == 0,
                "release_at": datetime.datetime.now()
                - datetime.timedelta(days=random.randint(3, 6)),
                "due_at": (
                    datetime.datetime.now()
                    + datetime.timedelta(days=random.randint(-2, 10))
                ),
                "subject": subject["id"],
            }
        )
priorities = ["low", "medium", "high"]

for i in range(
    announcements_per_classroom
    * len(data["classroom"])
    * announcements_per_subject
    * len(subject_teachers)
):
    data["announcement"].append(
        {
            "id": len(data["announcement"]) + 1,
            "title": f"Announcement {len(data['announcement'])}",
            "description": lorem,
            "is_active": len(data["announcement"]) % 2 == 0,
            "is_school_wide": False,
            "created_by": random.choice(data["teacher"])["id"],
            "signed_by": random.choice(data["teacher"])["id"],
            "release_at": datetime.datetime.now()
            - datetime.timedelta(days=random.randint(3, 6)),
            "expiry_at": (
                datetime.datetime.now()
                + datetime.timedelta(days=random.randint(-2, 10))
            ),
            "priority": random.choice(priorities),
            "classrooms": [],
            "subjects": [],
            "attachments": [],
        }
    )

for classroom in data["classroom"]:
    for announcement in random.choices(
        data["announcement"], k=announcements_per_classroom * len(data["classroom"]) * 2
    ):
        announcement["classrooms"].append(classroom["id"])

for subject in data["subject"]:
    for announcement in random.choices(
        data["announcement"], k=announcements_per_subject * len(data["subject"]) * 2
    ):
        announcement["subjects"].append(subject["id"])

for i in range(announcements_per_school):
    data["announcement"].append(
        {
            "id": len(data["announcement"]) + 1,
            "title": f"Announcement {len(data['announcement'])}",
            "description": lorem,
            "is_active": len(data["announcement"]) % 2 == 0,
            "is_school_wide": True,
            "created_by": random.choice(data["teacher"])["id"],
            "signed_by": random.choice(data["teacher"])["id"],
            "release_at": datetime.datetime.now()
            - datetime.timedelta(days=random.randint(3, 6)),
            "expiry_at": (
                datetime.datetime.now()
                + datetime.timedelta(days=random.randint(-2, 10))
            ),
            "priority": random.choice(priorities),
            "classrooms": [],
            "subjects": [],
            "attachments": [],
        }
    )

for m_name, values in data.items():
    with open(
        f"{dir_path}/dummy_data/{m_name.capitalize()}.csv",
        mode="w",
        newline="",
        encoding="utf-8",
    ) as output_file:
        fieldnames = list(values[0].keys())

        if "id" in fieldnames:
            fieldnames.remove("id")

        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in values:
            if "id" in row.keys():
                del row["id"]
            writer.writerow(row)

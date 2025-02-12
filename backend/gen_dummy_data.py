import csv
import datetime
import random
from django.contrib.auth.hashers import BCryptSHA256PasswordHasher
import os

class Config:
    def __init__(self):
        self.classrooms_len = 50
        self.teachers_per_subject = 3
        self.parents_len = 50
        self.students_per_classroom = 50
        self.announcements_per_subject = 5
        self.announcements_per_classroom = 5
        self.announcements_per_school = 10
        self.assignment_per_subject = 10
        self.standards = 10
        self.sections = 5
        self.subjects = {
            "Math": [],
            "Science": [],
            "English": [],
            "PT": [],
            "Social Studies": [],
        }
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.lorem = "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat."

class DataStore:
    def __init__(self):
        self.data = {
            "user": [],
            "classroom": [],
            "teacher": [],
            "parent": [],
            "student": [],
            "subject": [],
            "announcement": [],
            "assignment": [],
            "calendar": [],
            "event": [],
        }
        self.hasher = BCryptSHA256PasswordHasher()
        self.password = self.hasher.encode("Pass1234#", self.hasher.salt())

    def save_to_csv(self, config):
        for m_name, values in self.data.items():
            with open(
                f"{config.dir_path}/dummy_data/{m_name.capitalize()}.csv",
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

class UserGenerator:
    def __init__(self, data_store):
        self.data_store = data_store

    def add_user(self, username: str, email: str, first_name: str, last_name: str) -> int:
        user_id = len(self.data_store.data["user"]) + 1
        self.data_store.data["user"].append(
            {
                "id": user_id,
                "username": username,
                "email": email,
                "password": self.data_store.password,
                "first_name": first_name,
                "last_name": last_name,
                "school": 2,
            }
        )
        return user_id

class TeacherGenerator:
    def __init__(self, data_store, user_generator, config):
        self.data_store = data_store
        self.user_generator = user_generator
        self.config = config

    def add_teacher(self, teacher_num: int, subject: str) -> int:
        teacher_id = len(self.data_store.data["teacher"]) + 1
        user_id = self.user_generator.add_user(
            f"Teacher {teacher_num} for {subject}",
            f"teacher{teacher_num}for{subject}@testerp.com",
            f"Teacher {teacher_num}",
            f"For {subject}",
        )
        teacher = {
            "id": teacher_id,
            "user": user_id,
            "identifier": teacher_id + 69420,
            "phone": 8456123568 + user_id,
            "whatsapp": 9885456523 + user_id,
        }
        self.config.subjects[subject].append(teacher)
        self.data_store.data["teacher"].append(teacher)
        return user_id

    def generate_all_teachers(self):
        for subject in self.config.subjects.keys():
            for teacher_num in range(self.config.teachers_per_subject):
                self.add_teacher(teacher_num, subject)

class StudentGenerator:
    def __init__(self, data_store, user_generator):
        self.data_store = data_store
        self.user_generator = user_generator

    def add_guardian(self, student_id: int, guardian_num: int) -> int:
        user_id = self.user_generator.add_user(
            f"Guardian {guardian_num} for {student_id}",
            f"guardian{guardian_num}for{student_id}",
            f"Guardian {guardian_num}",
            f"For {student_id}",
        )
        guardian_id = len(self.data_store.data["parent"]) + 1
        self.data_store.data["parent"].append(
            {
                "id": guardian_id,
                "user": user_id,
                "identifier": 621 + guardian_id,
                "phone": 9898989898 + guardian_id,
                "whatsapp": 9898989898 + guardian_id,
            }
        )
        return guardian_id

    def add_student(self, student_num: int, standard: int, section: int) -> int:
        student_id = len(self.data_store.data["student"]) + 1
        user_id = self.user_generator.add_user(
            f"Student {student_num + 1} of Class {standard + 1}-{chr(ord('A') + section)}",
            f"student{student_num + 1}of_class{standard + 1}{chr(ord('A') + section)}@testerp.shouldnotexist.com",
            f"Student {student_num + 1}",
            f"For {standard + 1}-{chr(ord('A') + section)}",
        )
        self.data_store.data["student"].append(
            {
                "id": student_id,
                "user": user_id,
                "student_no": 621 + student_id,
                "roll_no": 42 + student_id,
                "guardian_1": self.add_guardian(student_id, 1),
                "guardian_2": self.add_guardian(student_id, 2),
            }
        )
        return student_id

class ClassroomGenerator:
    def __init__(self, data_store, student_generator, config):
        self.data_store = data_store
        self.student_generator = student_generator
        self.config = config

    def add_classroom(self, standard: int, section: int) -> int:
        classroom_id = len(self.data_store.data["classroom"]) + 1

        teachers = []
        for t in self.config.subjects.values():
            teachers.append(random.choice(t)["id"])

        for subject_name, s_teachers in self.config.subjects.items():
            teacher = None
            for s_teacher in map(lambda t: t["id"], s_teachers):
                if s_teacher in teachers:
                    teacher = s_teacher
                    break
            self.data_store.data["subject"].append(
                {
                    "id": len(self.data_store.data["subject"]) + 1,
                    "name": subject_name,
                    "is_active": len(self.data_store.data["subject"]) % 2 == 0,
                    "description": f"Subject {subject_name} of Classroom {standard + 1}{chr(ord('A') + section)}",
                    "classroom": classroom_id,
                    "teacher": teacher,
                }
            )

        class_teacher = teachers.pop()
        students = []

        for student_idx in range(random.randint(40, 45)):
            students.append(self.student_generator.add_student(student_idx, standard, section))

        self.data_store.data["classroom"].append(
            {
                "id": classroom_id,
                "name": f"Class {standard + 1}-{chr(ord('A') + section)}",
                "is_active": classroom_id % 2 == 0,
                "standard": standard + 1,
                "students": students,
                "class_teacher": class_teacher,
                "other_teachers": teachers,
            }
        )
        return classroom_id

    def generate_all_classrooms(self):
        for standard_idx in range(self.config.standards):
            for section_idx in range(self.config.sections):
                self.add_classroom(standard_idx, section_idx)

class ContentGenerator:
    def __init__(self, data_store, config):
        self.data_store = data_store
        self.config = config

    def generate_assignments(self):
        for subject in self.data_store.data["subject"]:
            for i in range(self.config.assignment_per_subject):
                self.data_store.data["assignment"].append(
                    {
                        "title": f"Assignment {i + 1} for {subject['name']}",
                        "description": f"Assignment description for assignment id {i + 1} for Subject: {subject['description']}",
                        "is_active": i % 2 == 0,
                        "release_at": datetime.datetime.now() - datetime.timedelta(days=random.randint(3, 6)),
                        "due_at": datetime.datetime.now() + datetime.timedelta(days=random.randint(-2, 10)),
                        "subject": subject["id"],
                    }
                )

    def generate_announcements(self):
        priorities = ["low", "medium", "high"]

        # Generate regular announcements
        for i in range(100):
            self.data_store.data["announcement"].append(
                {
                    "id": len(self.data_store.data["announcement"]) + 1,
                    "title": f"Announcement {len(self.data_store.data['announcement'])}",
                    "description": self.config.lorem,
                    "is_active": len(self.data_store.data["announcement"]) % 2 == 0,
                    "is_school_wide": False,
                    "created_by": random.choice(self.data_store.data["teacher"])["id"],
                    "signed_by": random.choice(self.data_store.data["teacher"])["id"],
                    "release_at": datetime.datetime.now() - datetime.timedelta(days=random.randint(3, 6)),
                    "expiry_at": datetime.datetime.now() + datetime.timedelta(days=random.randint(-2, 10)),
                    "priority": random.choice(priorities),
                    "classrooms": [],
                    "subjects": [],
                    "attachments": [],
                }
            )

        # Assign announcements to classrooms and subjects
        for classroom in self.data_store.data["classroom"]:
            for announcement in random.choices(self.data_store.data["announcement"], k=random.randint(2, 3)):
                announcement["classrooms"].append(classroom["id"])

        for subject in self.data_store.data["subject"]:
            for announcement in random.choices(self.data_store.data["announcement"], k=random.randint(2, 3)):
                announcement["subjects"].append(subject["id"])

        # Add school-wide announcements
        for i in range(self.config.announcements_per_school):
            self.data_store.data["announcement"].append(
                {
                    "id": len(self.data_store.data["announcement"]) + 1,
                    "title": f"School-wide Announcement {len(self.data_store.data['announcement'])}",
                    "description": self.config.lorem,
                    "is_active": len(self.data_store.data["announcement"]) % 2 == 0,
                    "is_school_wide": True,
                    "created_by": random.choice(self.data_store.data["teacher"])["id"],
                    "signed_by": random.choice(self.data_store.data["teacher"])["id"],
                    "release_at": datetime.datetime.now() - datetime.timedelta(days=random.randint(3, 6)),
                    "expiry_at": datetime.datetime.now() + datetime.timedelta(days=random.randint(-2, 10)),
                    "priority": random.choice(priorities),
                    "classrooms": [],
                    "subjects": [],
                    "attachments": [],
                }
            )

class CalendarGenerator:
    def __init__(self, data_store, config):
        self.data_store = data_store
        self.config = config

    def add_calendar(self, name, description, classrooms, subjects, users, is_school_wide):
        self.data_store.data["calendar"].append(
            {
                "id": len(self.data_store.data["calendar"]) + 1,
                "name": name,
                "description": description,
                "classrooms": classrooms,
                "subjects": subjects,
                "users": users,
                "is_school_wide": is_school_wide,
            }
        )

    def add_event(self, calendar, title, start, end):
        self.data_store.data["event"].append(
            {
                "id": len(self.data_store.data["event"]) + 1,
                "title": title,
                "start": start,
                "end": end,
            }
        )

    def generate_calendars_and_events(self):
        # Classroom calendars
        for classroom in self.data_store.data["classroom"]:
            subjects = random.choices(self.data_store.data["subject"], k=2)
            users = random.choices(self.data_store.data["user"], k=3)
            self.add_calendar(
                f"Calendar for {classroom['name']}",
                f"Calendar for classroom {classroom['name']}",
                [classroom["id"]],
                subjects,
                users,
                False,
            )

        # School-wide calendars
        for i in range(3):
            self.add_calendar(
                f"School Calendar {i+1}",
                f"School-wide calendar {i+1}",
                [], [], [], True,
            )

        # Generate events for each calendar
        for calendar in self.data_store.data["calendar"]:
            for i in range(random.randint(5, 10)):
                start_time = datetime.datetime(
                    hour=random.randint(7, 16),
                    day=10 + random.randint(1, 7),
                    month=2,
                    year=2025,
                )
                end_time = start_time + datetime.timedelta(hours=random.randint(1, 3))
                self.add_event(
                    calendar["id"],
                    f"Event {i+1} for {calendar['name']}",
                    start_time,
                    end_time,
                )

def main():
    config = Config()
    data_store = DataStore()
    user_generator = UserGenerator(data_store)
    teacher_generator = TeacherGenerator(data_store, user_generator, config)
    student_generator = StudentGenerator(data_store, user_generator)
    classroom_generator = ClassroomGenerator(data_store, student_generator, config)
    content_generator = ContentGenerator(data_store, config)
    calendar_generator = CalendarGenerator(data_store, config)

    # Generate all data
    teacher_generator.generate_all_teachers()
    classroom_generator.generate_all_classrooms()
    content_generator.generate_assignments()
    content_generator.generate_announcements()
    calendar_generator.generate_calendars_and_events()

    # Save to CSV
    data_store.save_to_csv(config)

if __name__ == "__main__":
    main()

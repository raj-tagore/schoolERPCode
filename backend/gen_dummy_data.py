import csv
import datetime
import random
from django.contrib.auth.hashers import BCryptSHA256PasswordHasher
import os
from faker import Faker
import uuid

class Config:
    def __init__(self):
        self.faker = Faker()
        self.classrooms_len = 50
        self.students_per_classroom = 50
        self.teachers_per_subject = 3
        self.guardians_per_student = 2
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
    def __init__(self, data_store, config):
        self.data_store = data_store
        self.config = config

    def add_user(self, role: str) -> int:
        """Generate a user with realistic data based on their role"""
        first_name = self.config.faker.first_name()
        last_name = self.config.faker.last_name()
        username = f"{first_name.lower()}.{last_name.lower()}"
        
        user_id = len(self.data_store.data["user"]) + 1
        self.data_store.data["user"].append(
            {
                "id": user_id,
                "username": f"{username}_{role}_{user_id}",
                "email": f"{username}_{user_id}@school.example.com",
                "password": self.data_store.password,
                "first_name": first_name,
                "last_name": last_name,
                "school": 2,
                "is_active": True,
                "is_staff": False,
                "is_superuser": False,
                "is_approved": True 
            }
        )
        return user_id

class TeacherGenerator:
    def __init__(self, data_store, user_generator, config):
        self.data_store = data_store
        self.user_generator = user_generator
        self.config = config

    def add_teacher(self, subject: str) -> int:
        teacher_id = len(self.data_store.data["teacher"]) + 1
        user_id = self.user_generator.add_user("teacher")
        
        teacher = {
            "id": teacher_id,
            "user": user_id,
            "identifier": self.config.faker.unique.random_number(digits=6),
            "phone": self.config.faker.numerify("+91##########"),
            "whatsapp": self.config.faker.numerify("+91##########"),
        }
        self.config.subjects[subject].append(teacher)
        self.data_store.data["teacher"].append(teacher)
        return user_id

    def generate_all_teachers(self):
        for subject in self.config.subjects.keys():
            for _ in range(self.config.teachers_per_subject):
                self.add_teacher(subject)

class GuardianGenerator:
    def __init__(self, data_store, user_generator, config):
        self.data_store = data_store
        self.user_generator = user_generator
        self.config = config

    def add_guardian(self) -> int:
        """Generate a guardian (parent) with realistic data"""
        guardian_id = len(self.data_store.data["parent"]) + 1
        user_id = self.user_generator.add_user("guardian")
        
        guardian = {
            "id": guardian_id,
            "user": user_id,
            "phone": self.config.faker.numerify("+91##########"),
            "whatsapp": self.config.faker.numerify("+91##########"),
        }
        
        self.data_store.data["parent"].append(guardian)
        return guardian_id

    def generate_guardians_for_student(self, student_id: int) -> tuple:
        """Generate two guardians for a student and return their IDs"""
        guardian1_id = self.add_guardian()
        guardian2_id = self.add_guardian()
        return (guardian1_id, guardian2_id)

class StudentGenerator:
    def __init__(self, data_store, user_generator, guardian_generator, config):
        self.data_store = data_store
        self.user_generator = user_generator
        self.guardian_generator = guardian_generator
        self.config = config

    def add_student(self, standard: int, section: int) -> int:
        student_id = len(self.data_store.data["student"]) + 1
        user_id = self.user_generator.add_user("student")
        
        # Generate guardians using GuardianGenerator
        guardian1_id, guardian2_id = self.guardian_generator.generate_guardians_for_student(student_id)
        
        self.data_store.data["student"].append(
            {
                "id": student_id,
                "user": user_id,
                "student_no": str(self.config.faker.unique.random_number(digits=6)),
                "roll_no": str(random.randint(1, 50)),
                "guardian_1": guardian1_id,
                "guardian_2": guardian2_id,
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

        # Select teachers for the classroom
        teachers = []
        for t in self.config.subjects.values():
            teachers.append(random.choice(t)["id"])

        # Create subjects for the classroom
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

        # Set class teacher and generate students
        class_teacher = teachers.pop()
        students = []

        for student_idx in range(random.randint(40, 45)):
            students.append(self.student_generator.add_student(standard, section))

        # Create classroom entry matching the model
        self.data_store.data["classroom"].append(
            {
                "id": classroom_id,
                "name": f"Class {standard + 1}-{chr(ord('A') + section)}",
                "is_active": classroom_id % 2 == 0,
                "standard": str(standard + 1),  # Changed to string as per model
                "students": students,
                "class_teacher": class_teacher,
                "other_teachers": teachers,
                "join_code": str(uuid.uuid4()),  # Added join_code field
            }
        )
        return classroom_id

    def generate_all_classrooms(self):
        for standard_idx in range(self.config.standards):
            for section_idx in range(self.config.sections):
                self.add_classroom(standard_idx, section_idx)

class AssignmentGenerator:
    def __init__(self, data_store, config):
        self.data_store = data_store
        self.config = config

    def generate_assignments(self):
        for subject in self.data_store.data["subject"]:
            for _ in range(self.config.assignment_per_subject):
                due_date = self.config.faker.date_time_between(
                    start_date='+1d',
                    end_date='+30d'
                )
                self.data_store.data["assignment"].append(
                    {
                        "title": self.config.faker.sentence(nb_words=6)[:50],  # Limit to max_length=50
                        "description": self.config.faker.text(max_nb_chars=500),
                        "is_active": random.choice([True, False]),
                        "release_at": due_date - datetime.timedelta(days=random.randint(5, 15)),
                        "due_at": due_date,
                        "subject": subject["id"],
                    }
                )

class AnnouncementGenerator:
    def __init__(self, data_store, config):
        self.data_store = data_store
        self.config = config
        self.priorities = ['low', 'medium', 'high']  # Matches model's PRIORITY_CHOICES

    def _create_announcement(self, is_school_wide: bool) -> dict:
        expiry_date = self.config.faker.date_time_between(
            start_date='+1d',
            end_date='+30d'
        )
        return {
            "id": len(self.data_store.data["announcement"]) + 1,
            "title": self.config.faker.sentence(nb_words=8)[:50],  # Limit to max_length=50
            "description": self.config.faker.text(max_nb_chars=1000),
            "is_active": random.choice([True, False]),
            "is_school_wide": is_school_wide,
            "created_by": random.choice(self.data_store.data["teacher"])["id"],
            "signed_by": random.choice(self.data_store.data["teacher"])["id"],
            "created_at": self.config.faker.date_time_between(
                start_date='-30d',
                end_date='now'
            ),
            "release_at": expiry_date - datetime.timedelta(days=random.randint(5, 15)),
            "expiry_at": expiry_date,
            "priority": random.choice(self.priorities),
            "classrooms": [],
            "subjects": [],
            "attachments": [],
        }

    def generate_all_announcements(self):
        # Generate regular announcements
        for _ in range(1000):
            announcement = self._create_announcement(False)
            self.data_store.data["announcement"].append(announcement)

        # Assign every announcement to 1-3 classrooms
        for announcement in self.data_store.data["announcement"]:
            classroom_ids = [classroom["id"] for classroom in random.sample(self.data_store.data["classroom"], k=random.randint(1, 3))]
            announcement["classrooms"] = classroom_ids

        # Generate school-wide announcements
        for _ in range(self.config.announcements_per_school):
            announcement = self._create_announcement(True)
            self.data_store.data["announcement"].append(announcement)

class CalendarGenerator:
    def __init__(self, data_store, config):
        self.data_store = data_store
        self.config = config

    def add_calendar(self, name: str, description: str, classrooms: list, subjects: list, is_school_wide: bool):
        self.data_store.data["calendar"].append(
            {
                "id": len(self.data_store.data["calendar"]) + 1,
                "name": name,
                "description": description,
                "classrooms": classrooms,
                "subjects": subjects,
                "is_school_wide": is_school_wide,
                "created_by": random.choice(self.data_store.data["teacher"])["id"],
            }
        )

    def add_event(self, calendar_id: int):
        start_time = self.config.faker.date_time_between(
            start_date='+1d',
            end_date='+90d'
        )
        duration_hours = random.randint(1, 8)
        
        self.data_store.data["event"].append(
            {
                "id": len(self.data_store.data["event"]) + 1,
                "calendar": calendar_id,
                "title": self.config.faker.sentence(nb_words=6),
                "start": start_time,
                "end": start_time + datetime.timedelta(hours=duration_hours),
                "attachment": None,
                "created_by": random.choice(self.data_store.data["teacher"])["id"],
            }
        )

    def generate_calendars(self):
        # Create one calendar per classroom
        # Not assigning any calendars to subjects
        for classroom in self.data_store.data["classroom"]:
            self.add_calendar(
                name=f"Calendar for {classroom['name']}",
                description=f"Calendar for classroom {classroom['name']}",
                classrooms=[classroom["id"]],
                subjects=[],
                is_school_wide=False
            )

        # Add a few school-wide calendars
        for i in range(3):
            self.add_calendar(
                name=f"School Calendar {i+1}",
                description=f"School-wide calendar {i+1}",
                classrooms=[],
                subjects=[],
                is_school_wide=True
            )

    def generate_events(self):
        # Generate 5-10 events for each calendar
        for calendar in self.data_store.data["calendar"]:
            for _ in range(random.randint(5, 10)):
                self.add_event(calendar["id"])

    def generate_calendars_and_events(self):
        self.generate_calendars()
        self.generate_events()


def main():
    config = Config()
    data_store = DataStore()
    
    # Initialize generators in dependency order
    user_generator = UserGenerator(data_store, config)
    guardian_generator = GuardianGenerator(data_store, user_generator, config)
    teacher_generator = TeacherGenerator(data_store, user_generator, config)
    student_generator = StudentGenerator(data_store, user_generator, guardian_generator, config)
    classroom_generator = ClassroomGenerator(data_store, student_generator, config)
    assignment_generator = AssignmentGenerator(data_store, config)
    announcement_generator = AnnouncementGenerator(data_store, config)
    calendar_generator = CalendarGenerator(data_store, config)

    # Generate all data
    teacher_generator.generate_all_teachers()
    classroom_generator.generate_all_classrooms()
    assignment_generator.generate_assignments()
    announcement_generator.generate_all_announcements()
    calendar_generator.generate_calendars_and_events()

    # Save to CSV
    data_store.save_to_csv(config)

if __name__ == "__main__":
    main()

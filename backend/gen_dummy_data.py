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
            "event": [],
            "purpose": [],
            "payee": [],
            "record": [],
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

class EventGenerator:
    def __init__(self, data_store, config):
        self.data_store = data_store
        self.config = config

    def add_event(self, classrooms: list = None, subjects: list = None, is_school_wide: bool = False):
        # Generate start dates between 30 days ago and 180 days in the future
        start_time = self.config.faker.date_time_between(
            start_date='-30d',
            end_date='+180d'
        )
        duration_hours = random.randint(1, 8)
        end_time = start_time + datetime.timedelta(hours=duration_hours)
        
        self.data_store.data["event"].append({
            "id": len(self.data_store.data["event"]) + 1,
            "title": self.config.faker.sentence(nb_words=6),
            "description": self.config.faker.text(max_nb_chars=500),
            "start": start_time,
            "end": end_time,
            "classrooms": classrooms or [],
            "subjects": subjects or [],
            "is_school_wide": is_school_wide,
            "attachment": None,
            "created_by": random.choice(self.data_store.data["teacher"])["id"],
        })

    def generate_events(self):
        # Generate classroom-specific events
        for classroom in self.data_store.data["classroom"]:
            # Generate 5-10 events per classroom
            for _ in range(random.randint(5, 10)):
                self.add_event(classrooms=[classroom["id"]], is_school_wide=False)

        # Generate school-wide events
        for _ in range(10):  # Generate 10 school-wide events
            self.add_event(is_school_wide=True)

class FinanceGenerator:
    def __init__(self, data_store, config):
        self.data_store = data_store
        self.config = config
        self.data_store.data["purpose"] = []
        self.data_store.data["payee"] = []
        self.data_store.data["record"] = []

    def generate_purposes(self):
        purposes = [
            ("Tuition Fee", "Regular tuition fee payment"),
            ("Library Fee", "Annual library membership fee"),
            ("Lab Fee", "Science and computer lab fee"),
            ("Sports Fee", "Sports equipment and facilities"),
            ("Transportation", "School bus transportation fee"),
        ]
        
        for name, description in purposes:
            self.data_store.data["purpose"].append({
                "name": name,
                "description": description,
            })

    def generate_payees(self):
        for _ in range(20):  # Generate 20 payees
            payee = {
                "account_id": str(uuid.uuid4()),
                "name": self.config.faker.name(),
                "email": self.config.faker.email(),
                "phone": self.config.faker.numerify("+91##########"),
                "card_id": uuid.uuid4().hex if random.choice([True, False]) else None,
                "wallet_id": uuid.uuid4().hex if random.choice([True, False]) else None,
                "bank_id": uuid.uuid4().hex if random.choice([True, False]) else None,
                "upi_id": f"{self.config.faker.user_name()}@upi" if random.choice([True, False]) else None,
            }
            self.data_store.data["payee"].append(payee)

    def generate_records(self):
        payment_types = ["netbanking", "card", "wallet", "upi"]
        payment_statuses = ["S", "P", "F"]
        
        for _ in range(1000):
            record = {
                "student": random.randrange(len(self.data_store.data["student"])) + 1,
                "amount": random.randint(1000, 50000),
                "datetime": self.config.faker.date_time_between(start_date="-1y"),
                "payment_type": random.choice(payment_types),
                "order_id": f"ORDER_{uuid.uuid4().hex[:8]}",
                "payment_status": random.choice(payment_statuses),
                "purpose": random.randrange(len(self.data_store.data["purpose"])) + 1,
                "payee": random.randrange(len(self.data_store.data["payee"])) + 1,
            }
            self.data_store.data["record"].append(record)

class ReportGenerator:
    def __init__(self, data_store, config):
        self.data_store = data_store
        self.config = config
        self.data_store.data["report_meta"] = []
        self.data_store.data["attendance_report"] = []

    def generate_reports(self):
        report_types = ["FE", "AT"]
        
        for _ in range(200):
            report_type = random.choice(report_types)
            submitted_by = random.choice(self.data_store.data["teacher"])["user"]
            is_approved = random.choice([True, False])
            
            report_meta = {
                "report_type": report_type,
                "submitted_by": submitted_by,
                "submitted_at": self.config.faker.date_time_between(start_date="-6m"),
                "attachment": None,
                "is_approved": is_approved,
                "approved_by": random.choice(self.data_store.data["teacher"])["user"] if is_approved else None,
                "approved_at": self.config.faker.date_time_between(start_date="-6m") if is_approved else None,
            }
            
            self.data_store.data["report_meta"].append(report_meta)
            
            if report_type == "AT":
                attendance_report = {
                    "metadata": len(self.data_store.data["report_meta"]),
                    "date": self.config.faker.date_between(start_date="-6m"),
                    "classroom": random.choice(self.data_store.data["classroom"])["name"],
                    "remarks": self.config.faker.text(max_nb_chars=200),
                }
                self.data_store.data["attendance_report"].append(attendance_report)

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
    event_generator = EventGenerator(data_store, config)
    finance_generator = FinanceGenerator(data_store, config)
    report_generator = ReportGenerator(data_store, config)

    # Generate all data
    teacher_generator.generate_all_teachers()
    classroom_generator.generate_all_classrooms()
    assignment_generator.generate_assignments()
    announcement_generator.generate_all_announcements()
    event_generator.generate_events()
    
    # Generate finance data
    finance_generator.generate_purposes()
    finance_generator.generate_payees()
    finance_generator.generate_records()
    
    # Generate reports
    report_generator.generate_reports()

    # Save to CSV
    data_store.save_to_csv(config)

if __name__ == "__main__":
    main()

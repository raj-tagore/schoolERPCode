import csv
import django
from django_tenants.utils import tenant_context

django.setup()

from users.models import User
from tenants.models import School
from accounts.models import Teacher, Parent, Student
from allocation.models import Classroom, Subject
from announcements.models import Announcement
from assignments.models import Assignment
from events.models import Event
from finances.models import Payee, Purpose, Record


tenant = School.objects.filter(name="school1")[0]

def process_csv(input_file, Model):
	reader = csv.DictReader(input_file)

	print(Model)
	for row in reader:
		m2m_fields = []
		temp_row = row.copy()
		for key in temp_row.keys():
			if key not in map(lambda field: field.name, Model._meta.get_fields()):
				del row[key]
		for field in Model._meta.get_fields():
			if field.many_to_many and field.name in row.keys():
				m2m_fields.append(( field.name, row[field.name] ))
				del row[field.name]
			elif (field.many_to_one or field.one_to_one) and field.name in row.keys():
				row[field.name + "_id"] = row[field.name]
				del row[field.name]

		with tenant_context(tenant):
			obj = Model.objects.create(**row)
			for field in m2m_fields:
				int_str = field[1].translate({ord('['): None, ord(']'): None}).split(",")
				if len(int_str) == 1 and int_str[0] == '':
					continue
				getattr(obj, field[0]).set([int(num) for num in int_str])

dummy_files = [
	("dummy_data/User.csv", User),
	("dummy_data/Teacher.csv", Teacher),
	("dummy_data/Parent.csv", Parent),
	("dummy_data/Student.csv", Student),
	("dummy_data/Classroom.csv", Classroom),
	("dummy_data/Subject.csv", Subject),
	("dummy_data/Announcement.csv", Announcement),
	("dummy_data/Assignment.csv", Assignment),
	("dummy_data/Event.csv", Event),
	("dummy_data/Payee.csv", Payee),
	("dummy_data/Purpose.csv", Purpose),
	("dummy_data/Record.csv", Record)
]


for input_csv_path, Model in dummy_files:
	with open(input_csv_path, mode='r', newline='', encoding='utf-8') as input_file:
		process_csv(input_file, Model)

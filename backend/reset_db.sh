#!/usr/bin/env bash

cd "$(dirname "$0")"

. ../venv/bin/activate


find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

touch {tenants,attachments,assessments,assignments,attendance,accounts,users,announcements,allocation}/migrations/__init__.py

doas -u postgres psql -c "DROP DATABASE \"schoolERPDB\";"

doas -u postgres psql -c "CREATE DATABASE \"schoolERPDB\";"

python manage.py makemigrations

python manage.py migrate

printf "public\nlocalhost\nlocalhost\n\n" | python manage.py create_tenant

printf "school1\nschool1\nschool1.localhost\n\n" | python manage.py create_tenant

export DJANGO_SUPERUSER_USERNAME=sandy
export DJANGO_SUPERUSER_PASSWORD=san
export DJANGO_SUPERUSER_EMAIL=san@san.com
export DJANGO_SETTINGS_MODULE=schoolERPCode.settings

python manage.py createsuperuser --noinput

doas -u postgres psql -c "INSERT INTO auth_group VALUES (1, 'Admin')" "schoolERPDB"
doas -u postgres psql -c "INSERT INTO auth_group VALUES (2, 'Teacher')" "schoolERPDB"
doas -u postgres psql -c "INSERT INTO auth_group VALUES (3, 'Student')" "schoolERPDB"
doas -u postgres psql -c "INSERT INTO auth_group VALUES (4, 'Parent')" "schoolERPDB"

python <<HEREDOC
import csv
import sys
from django.contrib.auth.hashers import make_password
import django
from django_tenants.utils import tenant_context

django.setup()

from users.models import User
from tenants.models import School
from accounts.models import Teacher, Parent, Student
from allocation.models import Classroom, Subject
from announcements.models import Announcement

tenant = School.objects.filter(name="school1")[0]

def process_csv(input_file, Model):
	reader = csv.DictReader(input_file)
	fieldnames = reader.fieldnames


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
				try:
					getattr(obj, field[0]).set([int(num) for num in field[1].split(",")])
				except:
					print("M2M setting error")

dummy_files = [
	("dummy_data/User.csv", User),
	("dummy_data/Teacher.csv", Teacher),
	("dummy_data/Parent.csv", Parent),
	("dummy_data/Student.csv", Student),
	("dummy_data/Classroom.csv", Classroom),
	("dummy_data/Subject.csv", Subject),
	("dummy_data/Announcement.csv", Announcement),
]


for input_csv_path, Model in dummy_files:
	with open(input_csv_path, mode='r', newline='', encoding='utf-8') as input_file:
		process_csv(input_file, Model)
HEREDOC

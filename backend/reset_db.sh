#!/usr/bin/env bash

cd "$(dirname "$0")"



find . -path "*/migrations/*.py" -not -name "*__init__*.py" -delete

touch {tenants,attachments,assessments,assignments,attendance,accounts,users,announcements,allocation}/migrations/__init__.py

if command -v doas &> /dev/null; then
    SUPER="doas"
else
    SUPER="sudo"
fi

if command -v uv &> /dev/null; then
    PYTHON_RUNNER="uv run"
else
	. ../venv/bin/activate
    PYTHON_RUNNER="python"
fi

echo "Using: $SUPER"
echo "Using: $PYTHON_RUNNER"

$SUPER -u postgres psql -c "DROP DATABASE \"schoolERPDB\";"

$SUPER -u postgres psql -c "CREATE DATABASE \"schoolERPDB\";"

$PYTHON_RUNNER manage.py makemigrations

$PYTHON_RUNNER manage.py migrate

printf "public\nlocalhost\nlocalhost\n\n" | $PYTHON_RUNNER manage.py create_tenant

printf "school1\nschool1\nschool1.localhost\n\n" | $PYTHON_RUNNER manage.py create_tenant

export DJANGO_SETTINGS_MODULE=schoolERPCode.settings


$SUPER -u postgres psql -c "INSERT INTO auth_group VALUES (1, 'Admin')" "schoolERPDB"
$SUPER -u postgres psql -c "INSERT INTO auth_group VALUES (2, 'Teacher')" "schoolERPDB"
$SUPER -u postgres psql -c "INSERT INTO auth_group VALUES (3, 'Student')" "schoolERPDB"
$SUPER -u postgres psql -c "INSERT INTO auth_group VALUES (4, 'Parent')" "schoolERPDB"

$PYTHON_RUNNER import_dummy_data.py 2> /dev/null

export DJANGO_SUPERUSER_USERNAME=sandy
export DJANGO_SUPERUSER_PASSWORD=san
export DJANGO_SUPERUSER_EMAIL=san@san.com

$PYTHON_RUNNER manage.py createsuperuser --noinput

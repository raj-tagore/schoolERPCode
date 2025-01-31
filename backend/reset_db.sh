#!/usr/bin/env bash

cd "$(dirname "$0")"

. ../venv/bin/activate


find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

touch {tenants,attachments,assessments,assignments,attendance,accounts,users,announcements,allocation}/migrations/__init__.py

if command -v doas &> /dev/null; then
    SUPER="doas"
else
    SUPER="sudo"
fi

echo "Using: $SUPER"

$SUPER -u postgres psql -c "DROP DATABASE \"schoolERPDB\";"

$SUPER -u postgres psql -c "CREATE DATABASE \"schoolERPDB\";"

python manage.py makemigrations

python manage.py migrate

printf "public\nlocalhost\nlocalhost\n\n" | python manage.py create_tenant

printf "school1\nschool1\nschool1.localhost\n\n" | python manage.py create_tenant

export DJANGO_SETTINGS_MODULE=schoolERPCode.settings


$SUPER -u postgres psql -c "INSERT INTO auth_group VALUES (1, 'Admin')" "schoolERPDB"
$SUPER -u postgres psql -c "INSERT INTO auth_group VALUES (2, 'Teacher')" "schoolERPDB"
$SUPER -u postgres psql -c "INSERT INTO auth_group VALUES (3, 'Student')" "schoolERPDB"
$SUPER -u postgres psql -c "INSERT INTO auth_group VALUES (4, 'Parent')" "schoolERPDB"

python import_dummy_data.py 2> /dev/null

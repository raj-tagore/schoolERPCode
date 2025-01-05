#!/usr/bin/env bash

cd "$(dirname "$0")"

. ../venv/bin/activate

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

doas -u postgres psql -c "DROP DATABASE \"schoolERPDB\";"

doas -u postgres psql -c "CREATE DATABASE \"schoolERPDB\";"

python manage.py makemigrations

python manage.py migrate

printf "public\nlocalhost\nlocalhost\n\n" | python manage.py create_tenant

printf "school1\nschool1\nschool1.localhost\n\n" | python manage.py create_tenant

export DJANGO_SUPERUSER_USERNAME=sandy
export DJANGO_SUPERUSER_PASSWORD=san
export DJANGO_SUPERUSER_EMAIL=san@san.com

python manage.py createsuperuser --noinput




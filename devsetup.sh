#!/bin/bash

export DJANGO_SUPERUSER_USERNAME="vscode"
export DJANGO_SUPERUSER_EMAIL="example@example.com"
export DJANGO_SUPERUSER_PASSWORD="vscode"
devdatabase="/workspaces/digital_library_tracker/db.sqlite3"

rm "${devdatabase:?}" 
python3 manage.py migrate
python3 manage.py loaddata developer
python3 manage.py loaddata publisher
python3 manage.py createsuperuser --noinput
#!/bin/bash

export DJANGO_SUPERUSER_USERNAME="vscode"
export DJANGO_SUPERUSER_EMAIL="example@example.com"
export DJANGO_SUPERUSER_PASSWORD="vscode"
export DEBUG="True"
export SECRET_KEY="devsetup_key"
export ALLOWED_HOSTS='*'
devdatabase="/workspaces/digital_library_tracker/db.sqlite3"

clean () {
    rm "${devdatabase:?}" 
}

migrate () {
    python3 manage.py migrate
    python3 manage.py loaddata developer
    python3 manage.py loaddata publisher
}

usersetup () {
    python3 manage.py createsuperuser --noinput
}

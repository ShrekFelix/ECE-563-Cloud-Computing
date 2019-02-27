python manage.py migrate Actiondex zero
rm -rf Actiondex/migrations/*
python manage.py makemigrations Actiondex
python manage.py migrate

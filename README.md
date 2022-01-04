# Task-Scheduler
    Scheduler.

# In this project I use.
    1. Django==3.2.6
    2. django-celery-beat
    3. djangorestframework-simplejwt
    4. django-redis==5.0.0


# Create venv
    python3 -m venv venv

# activate
    source env/bin/activate

# install packages
    pip install -r requirements.txt

# create migrations and superuser
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsupeuser

# Run this command two show result
        activate docker

    1.  docker-compose up   
    2.  celery -A Task beat
    3.  celery -A Task worker -l INFO
    4.  python manage.py runserver

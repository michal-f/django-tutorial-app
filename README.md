# django tutorial - Polls App #


##**Content:**

- Django tutorial App Polls


##**Implemented features:**

- User registration and login handler

- Bootstrap 4 

- Dynamic requests

- Multilinguality


##**Installation:**

    pip install -r requirements.txt


##**Initial settings:**

    python manage.py migrate


##**Start:**

    python manage.py runserver


---

#####Languages Translation Update

    python manage.py makemessages -l de
    python manage.py makemessages -l pl
    python manage.py makemessages -d djangojs -l pl
    python manage.py makemessages -d djangojs -l de
    python manage.py compilemessages

#####Languages Flags fixtures loading

    python manage.py loaddata languages_flags

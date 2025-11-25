# hr-data-normalizer-django
practice repo for python django data

**set up Python env + install DJango/DRF**
`python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install --upgrade pip
pip install django djangorestframework`

**Initialize the Django project inside the repo:**
`django-admin startproject hrdata .
python manage.py startapp core`

**Create employee and enrollment models (like RoR but Django)**
`models.py`
*then migrate the models into the database*
`python manage.py makemigrations
python manage.py migrate`

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

**Seed CSV + Import Logic (Django-ified version of POPOs plain old ruby/python objects)**
`core/management/comands/import_hr_data.py`
run it `python manage.py import_hr_data`

**Add Django REST Framework: Serializers + viewsets**
`core/serializers.py`
`core/views.py`
*wire up URLs*
`core/urls.py`
`hrdata/urls.py`
*run dev server*
`python manage.py runserver`
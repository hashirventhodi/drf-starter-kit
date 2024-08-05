# DRF Starter Kit

## Overview
This project is a clinic management system built using Django. It provides functionalities for managing patients, appointments, doctors, and more.

## Installation
1. Clone the repository
2. Create a virtual environment and activate it:
```
python -m venv .venv
. .venv/bin/activate
```
4. Install dependencies
```
pip install -r requirements.txt
```
3. Create New App
```
python manage.py startapp <app_name>
```
4. Run Project
```
python manage.py runserver     
```
5. Create Super User
```
python manage.py createsuperuser
```
7. Make Migrations
```
python manage.py makemigrations
```
8. Run Migration
```
python manage.py migrate
```
9. Hep
```
python manage.py
django-admin
```

## Usage
- Access the admin interface at `http://localhost:8000/admin/` to manage data.
- Use the API endpoints for programmatic access.


## Project Structure
```
project_name/
│
├── apps/
│   ├── app1/
│   │   ├── v1/
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   └── urls.py
│   │   ├── models.py
│   │   └── tests.py
│   ├── app2/
│   │   └── ...
│   └── ...
│
├── core/
│   ├── settings/
│   │   ├── base.py           # Base settings
│   │   ├── development.py    # Development settings
│   │   └── production.py     # Production settings
│   ├── urls.py               # Root URL configuration
│   └── wsgi.py               # WSGI config for deployment
│
├── utils/
│   ├── mixins.py             # Utility mixins
│   ├── permissions.py        # Custom permissions
│   └── ...                   # Other utility files
│
├── manage.py                  # Django's command-line utility
├── requirements/              # Directory for requirements files
│   ├── base.txt              # Base dependencies
│   ├── development.txt       # Development environment dependencies
│   └── production.txt        # Production environment dependencies
│
├── README.md                  # Project documentation
├── LICENSE                    # License information
└── .gitignore                 # Git ignore file


```

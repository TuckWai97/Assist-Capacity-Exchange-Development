# Assist Capacity Exchange Development


## Prerequisite:

1. Download Python from official ( Python 3.8 or later for Django 4.2)
https://www.python.org/downloads/

    - To check which Python version to use with Django 

      https://docs.djangoproject.com/en/4.2/faq/install/#faq-python-version-support
2. Download pip 
   - `python3 -m pip install --upgrade pip`

3. Download Django
4. **Optional**: Use Django crispy form with Bootstrap 5 
    - `pip install crispy-bootstrap5`

      Refer to github repo here to use it: 

https://github.com/django-crispy-forms/crispy-bootstrap5/tree/main
## Before doing the task:
1. It is recommended for you to use virtual environment
    - `py -m venv env`

      env is your virtual environment name, you can name it as you wish.

2. Activate your virtual environment in Windows

    -  `\env\Scripts\activate`

        'env' is your previous created virtual environment name.

**Note**: You can refer to documentation here: https://docs.python.org/3/tutorial/venv.html

3. Check django version ,also can check whether Django is installed.  
    -  `python -m django --version`

4. If not installed, install Django.
    - `python -m pip install Django`

5. Make sure to install requests library, because it is needed in the task.
    - `python3 -m pip install requests`

## Tasks
## Task 1: Create a Django project and commit it to GitHub
### Objective of the task: Create a Django project with an app called bug and commit it in GitHub.
Steps:
1. Read the first part of the Writing your first Django app tutorial.
2. Create a Django project with an app called bug. We recommend you use PyCharm, but if you are familiar with other IDEs, you are welcomed to use them instead.

## Task 2: Structure the database and create a model
### Objective of the task: Structure a SQLite database and create a django model for the Bug app
Steps:
1. Read the second part of the Writing your first Django app tutorial.
2. Create a Bug model with the following fields: "description", "bug_type", "report_date", "status", representing, respectivelly, the textual description of the bug, the type of the bug (e.g. error, new feature etc), the date in which the bug is being registered and the status of resolution of the bug (e.g. to do, in progress, done, etc).
3. Structure the database as described in the tutorial and create at least one bug through Django Admin.

## Task 3: Write views and templates.
### Objective of the task: Create views and templates to 1) register and view a bug and 2) list all bugs registered
Steps:

1. Read the third and fourth parts of the Writing your first Django app tutorial.
2. Create one view to register a bug into the database.
   - Create a html template with a simple form to add the bug to database.
3. Create another view to view the fields of the bug.
   - Create a html template with a simple list of the fields of the bug.
4. And finally, create a view to list all the bugs in the database.
   - Create a html template with a simple list with links to the detail page of each bug.

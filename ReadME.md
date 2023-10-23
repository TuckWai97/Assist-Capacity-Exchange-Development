# Assist Capacity Exchange Development


Prequisites:
1. Download Python from official https://www.python.org/downloads/ ,Python 3.8 or later for Django 4.2
  - To check which Python version to use with Django https://docs.djangoproject.com/en/4.2/faq/install/#faq-python-version-support
2. Download pip py -m pip install --upgrade pip
2.  python -m pip install Django 
3. **Optional**: Use Django crispy form with Bootstrap 5 
  - pip install crispy-bootstrap5
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

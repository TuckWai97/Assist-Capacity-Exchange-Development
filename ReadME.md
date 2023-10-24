# Assist Capacity Exchange Development


## Prerequisite:

1. Download Python from official ( Python 3.8 or later for Django 4.2)
https://www.python.org/downloads/

>    Note: To check which Python version to use with Django 
>       https://docs.djangoproject.com/en/4.2/faq/install/#faq-python-version-support
2. Download pip (if using venv, it is included)
   ```bash
   python3 -m pip install --upgrade pip
   ```
3. Download Django (can download when in venv)
4. **Optional**: Use Django crispy form with Bootstrap 5 
   
> Refer to github repo here to use it: 
>  https://github.com/django-crispy-forms/crispy-bootstrap5/tree/main

### Setup in your machine:
1. Clone using git command at terminal *OR* download `zip` by clicking `<>code` button on my github repository and choose `Download ZIP` to your computer then open it using IDE
    ```bash
    git clone https://github.com/factism001/wikimedia.git
    ```
2. change directory into `project` directory
   ```bash
   cd project
   ```
3. Create a virtual environment to isolate project dependencies
   ```bash
   python -m venv env
   ```
    >    env is your virtual environment name, you can name it as you wish.

4. Activate your virtual environment
   - For Windows
      - If use cammand.exe
           ```bash    
          - \env\Scripts\activate.bat
           ```
      - Powershell
           ``` bash
          - \env\Scripts\Activate.ps1
           ```
    >    'env' is your previous created virtual environment name.
    > **Note**: You can refer to documentation here: https://docs.python.org/3/tutorial/venv.html


5. Use pip to install the required dependencies and packages.
   ```bash
   pip install -r requirements.txt
   ```
### How does the project works?
1. Start the development server.
   ```bash
   python manage.py runserver
    ```
2. Open web browser, go to 127.0.0.1:8000/ for home page.

3. Go to http://127.0.0.1:8000/register/ for registering a bug with description, bug_type, report_date and status.

4. Go to http://127.0.0.1:8000/<bug_id> for checking the bug details.

5. Go to http://127.0.0.1:8000/list/ to view the bug list with link for each bug.

### Feature of the Django website:
- Home page: Landing page with 2 buttons, `Register Bug` and `View Bug list`
- Bug register page: Bug field with `description`, `bug_type`, `report_date` and `status`.
- Bug detail page : Shows the bug details submitted.
- Bug List page :Links to the submitted bugs.
- Django admin page : Used by admin to create, remove and modify bug.

### Django Admin
1. Create a user who can login into admin site using the command:
    ``` bash
    python manage.py createsuperuser
    ```
2. Enter desired username, email address, and password. You will be asked to enter your password twice, the second time as a confirmation of the first.

3. Start development server if it is not running.
    ```bash
    python manage.py runserver
    ```
4. Open a web browser, go to http://127.0.0.1:8000/admin/ to access it.

5. Login with superuser account that you created previously.

6. You can perform 2 actions:

    - :heavy_plus_sign: ``Add`` bug with filling up the details, then click ``Save``

    - :pencil2: ``Change`` bug details or Delete it
   > info at https://docs.djangoproject.com/en/4.2/intro/tutorial02/ near end of page


## Tasks
## Task 1: Create a Django project and commit it to GitHub
### Objective of the task: Create a Django project with an app called bug and commit it in GitHub.
Steps:
1. Read the [first part of the Writing your first Django app](https://docs.djangoproject.com/en/4.2/intro/tutorial01/) tutorial.

2. Create a Django project with an app called bug. We recommend you use PyCharm, but if you are familiar with other IDEs, you are welcomed to use them instead.

## Task 2: Structure the database and create a model
### Objective of the task: Structure a SQLite database and create a django model for the Bug app
Steps:
1. Read the [second part of the Writing your first Django app](https://docs.djangoproject.com/en/4.2/intro/tutorial02/) tutorial.

2. Create a Bug model with the following fields: "description", "bug_type", "report_date", "status", representing, respectivelly, the textual description of the bug, the type of the bug (e.g. error, new feature etc), the date in which the bug is being registered and the status of resolution of the bug (e.g. to do, in progress, done, etc).

3. Structure the database as described in the tutorial and create at least one bug through Django Admin.
Output:

## Task 3: Write views and templates.
### Objective of the task: Create views and templates to 1) register and view a bug and 2) list all bugs registered
Steps:

1. Read the [third](https://docs.djangoproject.com/en/4.2/intro/tutorial03/) and [fourth](https://docs.djangoproject.com/en/4.2/intro/tutorial04/) parts of the Writing your first Django app tutorial.

2. Create one view to register a bug into the database.
   - Create a html template with a simple form to add the bug to database.

3. Create another view to view the fields of the bug.
   - Create a html template with a simple list of the fields of the bug.

4. And finally, create a view to list all the bugs in the database.
   - Create a html template with a simple list with links to the detail page of each bug.

## Task 4: Develop automated unit tests
### Objective of the task: Create automated unit tests for the bug app
Steps:

1. Read the fifth part of the [Writing your first Django app](https://docs.djangoproject.com/en/4.2/intro/tutorial05/) tutorial.

2. Create at least four automated tests of the bug model.

3. Create at least three automated tests of the bug views

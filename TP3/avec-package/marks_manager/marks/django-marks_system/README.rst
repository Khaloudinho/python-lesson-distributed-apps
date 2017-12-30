=====
Polls
=====

Marks_system is a simple Django app to conduct Web-based Marks_system. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
    'marks_system.apps.MarksSystemConfig',
        ...
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('marks-system/', include('marks_system.urls'))

3. Run `python3 manage.py migrate` to create the Marks_system models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a marks_system (you'll need the Admin app enabled). create a user if you haven't.

5. Visit http://127.0.0.1:8000/marks-system/ to participate in the marks-sytem application.
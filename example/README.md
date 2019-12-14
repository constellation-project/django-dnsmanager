# Running a demo project

We assume that you are using Debian Stretch or Buster and this package is
installed via pip in your Python 3 environment.

Clone the project and go to `example_project` directory.

Now we need to create the database tables and an admin user.
Run the following and when prompted to create a
superuser choose yes and follow the instructions:

```bash
$ ./manage.py migrate
$ ./manage.py createsuperuser
```

Now you need to run the Django development server:

```
$ ./manage.py runserver
```

You should then be able to open your browser on <http://127.0.0.1:8000> and see
this app running.

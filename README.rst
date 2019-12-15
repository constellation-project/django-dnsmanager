.. image::  https://travis-ci.com/erdnaxe/django-dnsmanager.svg?branch=master
    :target: http://travis-ci.com/erdnaxe/django-dnsmanager
.. image:: https://img.shields.io/codecov/c/github/erdnaxe/django-dnsmanager/master.svg
    :target: https://codecov.io/github/erdnaxe/django-dnsmanager?branch=master

Django DNS manager
==================

This is a DNS manager Django app.

Manual install
--------------

For development in a virtualenv:

.. code:: bash

   $ python3 -m venv venv
   $ source venv/bin/activate
   $ pip3 install -e .

Running a demo project
----------------------

We assume this package is installed in your Python 3 environment.

Clone the project and go to ``example_project`` directory.

Now we need to create the database tables and an admin user. Run the
following and follow the instructions:

.. code:: bash

   $ ./manage.py migrate
   $ ./manage.py createsuperuser

Now you may run the Django development server:

::

   $ ./manage.py runserver

You should then be able to open your browser on http://127.0.0.1:8000
and see this app running.

License
-------

Django-dnsmanager uses the same license as Django (BSD-like)
because we believe in open development.
Please see LICENSE file for more details.

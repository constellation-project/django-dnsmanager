.. image::  https://travis-ci.com/erdnaxe/django-dnsmanager.svg?branch=master
    :target: http://travis-ci.com/erdnaxe/django-dnsmanager
.. image:: https://img.shields.io/codecov/c/github/erdnaxe/django-dnsmanager/master.svg
    :target: https://codecov.io/github/erdnaxe/django-dnsmanager?branch=master

Django DNS manager
==================

This is a DNS manager Django app.

Installation
------------

The following lines creates a Python3 virtualenv and installs
``django-dnsmanager`` inside.

.. code:: bash

   $ python3 -m venv venv
   $ source venv/bin/activate
   $ pip install django-dnsmanager

Features
--------

* Polymorphic models based on
  [Django Polymorphic](https://github.com/django-polymorphic/django-polymorphic) ;
* Integration with Django Contrib Admin and AdminDocs ;
* Integration with Django Rest Framework ;
* Generation of ready to use zone files.

This app targets Django 1.11 (current Debian version), 2.2 (last LTS) and 3.0.
It runs on Python 3.6 and Python 3.7.

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

.. code:: bash

   $ ./manage.py runserver

You should then be able to open your browser on http://127.0.0.1:8000
and see this app running.

License
-------

Django-dnsmanager uses the same license as Django (BSD-like)
because we believe in open development.
Please see LICENSE file for more details.

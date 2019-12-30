Django DNS manager
==================

|travis| |coverage| |github_version| |pypi_version| |django_version| |doc|

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
  `Django Polymorphic <https://github.com/django-polymorphic/django-polymorphic>`_ ;
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

.. |travis| image:: https://img.shields.io/travis/com/constellation-project/django-dnsmanager/master?style=flat-square
    :target: https://travis-ci.com/constellation-project/django-dnsmanager

.. |coverage| image:: https://img.shields.io/codecov/c/github/constellation-project/django-dnsmanager/master.svg?style=flat-square
    :target: https://codecov.io/github/constellation-project/django-dnsmanager?branch=master

.. |github_version| image:: https://img.shields.io/github/v/tag/constellation-project/django-dnsmanager?style=flat-square
    :target: https://github.com/constellation-project/django-dnsmanager/releases/latest

.. |pypi_version| image:: https://img.shields.io/pypi/v/django-dnsmanager?style=flat-square
    :target: https://pypi.org/project/django-dnsmanager/

.. |django_version| image:: https://img.shields.io/pypi/djversions/django-dnsmanager?style=flat-square
    :target: https://pypi.org/project/django-dnsmanager/

.. |doc| image:: https://img.shields.io/readthedocs/django-dnsmanager?style=flat-square
    :target: http://django-dnsmanager.readthedocs.io

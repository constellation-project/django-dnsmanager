Contributing
============

Manual installation
-------------------

For development in a virtualenv, git clone this project and then:

.. code:: bash

   $ python3 -m venv venv
   $ source venv/bin/activate
   $ pip install -e .
   $ pip install djangorestframework docutils

``djangorestframework`` and ``docutils`` are not required but useful if
you want a REST API and a documentation in Django Admin.

Package to pip
--------------

To package a new version to pip:

.. code:: bash

   $ source venv/bin/activate
   $ pip install setuptools wheel twine
   $ cd dnsmanager && django-admin compilemessages && cd ..
   $ python setup.py sdist bdist_wheel
   $ twine upload dist/*

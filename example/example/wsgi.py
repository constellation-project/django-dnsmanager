# -*- mode: python; coding: utf-8 -*-
# Copyright (C) 2016-2019 by Cr@ns
# SPDX-License-Identifier: GPL-3.0-or-later

"""
WSGI config for this example project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'example.settings')

application = get_wsgi_application()

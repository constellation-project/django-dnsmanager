#!/usr/bin/env python3
# -*- mode: python; coding: utf-8 -*-
# Copyright (C) 2016-2019 by Cr@ns
# SPDX-License-Identifier: GPL-3.0-or-later

import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'example.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

# -*- mode: python; coding: utf-8 -*-
# Copyright (C) 2016-2019 by Cr@ns
# SPDX-License-Identifier: GPL-3.0-or-later

import pkg_resources

try:
    __version__ = pkg_resources.require("django-dnsmanager")[0].version
except pkg_resources.DistributionNotFound:
    __version__ = None  # for RTD among others

default_app_config = 'dnsmanager.apps.DnsManagerConfig'

# -*- mode: python; coding: utf-8 -*-
# Copyright (C) 2016-2019 by Cr@ns
# SPDX-License-Identifier: GPL-3.0-or-later

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    # No app, so redirect to admin
    url(r'^$', RedirectView.as_view(pattern_name='admin:index'), name='index'),

    # Include Django Contrib and Core routers
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/profile/',
        RedirectView.as_view(pattern_name='index')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
]

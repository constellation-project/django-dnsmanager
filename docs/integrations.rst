Integrations
============

Integration with Django Rest Framework
--------------------------------------

This app brings serializers and viewsets for Django Rest Framework.
You can use those in your REST API like this,

.. code:: python3

    from django.conf.urls import include, url
    from rest_framework import routers
    from dnsmanager.api import views

    router = routers.DefaultRouter()
    router.register(r'record', views.RecordViewSet)
    router.register(r'zone', views.ZoneViewSet)

    urlpatterns += [
        url(r'^api/', include(router.urls)),
    ]

Views
*****

.. automodule:: dnsmanager.api.views
   :members:
   :undoc-members:
   :show-inheritance:

Serializers
***********

.. automodule:: dnsmanager.api.serializers
   :members:
   :undoc-members:
   :show-inheritance:

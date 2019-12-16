from django.conf.urls import url

from .views import ZoneDetailView

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', ZoneDetailView.as_view(content_type='text/plain'), name='zone-detail'),
]

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.detail import DetailView

from .models import Zone


class ZoneDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ('dnsmanager.view_zone', 'dnsmanager.view_record')
    model = Zone

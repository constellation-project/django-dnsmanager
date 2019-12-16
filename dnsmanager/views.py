from django.views.generic.detail import DetailView

from .models import Zone


class ZoneDetailView(DetailView):
    model = Zone

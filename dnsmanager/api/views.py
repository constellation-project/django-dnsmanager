from rest_framework import viewsets

from .serializers import RecordPolymorphicSerializer, ZoneSerializer
from ..models import Record, Zone


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordPolymorphicSerializer


class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer

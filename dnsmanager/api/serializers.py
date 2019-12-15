from rest_framework import serializers

from .polymorphic_serializer import PolymorphicSerializer
from ..models import A, AAAA, CNAME, MX, NS, PTR, SOA, SRV, TXT, Zone


class ASerializer(serializers.ModelSerializer):
    class Meta:
        model = A
        fields = '__all__'


class AAAASerializer(serializers.ModelSerializer):
    class Meta:
        model = AAAA
        fields = '__all__'


class CNAMESerializer(serializers.ModelSerializer):
    class Meta:
        model = CNAME
        fields = '__all__'


class MXSerializer(serializers.ModelSerializer):
    class Meta:
        model = MX
        fields = '__all__'


class NSSerializer(serializers.ModelSerializer):
    class Meta:
        model = NS
        fields = '__all__'


class PTRSerializer(serializers.ModelSerializer):
    class Meta:
        model = PTR
        fields = '__all__'


class SOASerializer(serializers.ModelSerializer):
    class Meta:
        model = SOA
        fields = '__all__'


class SRVSerializer(serializers.ModelSerializer):
    class Meta:
        model = SRV
        fields = '__all__'


class TXTSerializer(serializers.ModelSerializer):
    class Meta:
        model = TXT
        fields = '__all__'


class RecordPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        A: ASerializer,
        AAAA: AAAASerializer,
        CNAME: CNAMESerializer,
        MX: MXSerializer,
        NS: NSSerializer,
        PTR: PTRSerializer,
        SOA: SOASerializer,
        SRV: SRVSerializer,
        TXT: TXTSerializer,
    }


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = '__all__'

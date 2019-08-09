from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from polymorphic.models import PolymorphicModel


class RecordNameField(models.CharField):

    record_name_validator = RegexValidator(
        regex=r'(?:[a-zA-Z0-9_][a-zA-Z0-9_-]{0,62}(?<!-)\.)*(?:[a-zA-Z0-9_][a-zA-Z0-9_-]{0,62}(?<!-))',
        message='Not a valid domain name',
    )

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 253
        if 'editable' not in kwargs:
            kwargs['editable'] = True
        if 'validators' in kwargs:
            kwargs['validators'].append(RecordNameField.record_name_validator)
        else:
            kwargs['validators'] = [RecordNameField.record_name_validator]
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['max_length']
        if 'validators' in kwargs:
            if RecordNameField.record_name_validator in kwargs['validators']:
                kwargs['validators'].remove(RecordNameField.record_name_validator)
            if not kwargs['validators']:
                del kwargs['validators']
        return name, path, args, kwargs

class DomainNameField(models.CharField):

    domain_name_validator = RegexValidator(
        regex=r'(?:[a-zA-Z0-9][a-zA-Z0-9-]{0,62}(?<!-)\.)*(?:[a-zA-Z0-9][a-zA-Z0-9-]{0,62}(?<!-))',
        message='Not a valid domain name',
    )

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 253
        if 'editable' not in kwargs:
            kwargs['editable'] = True
        if 'validators' in kwargs:
            kwargs['validators'].append(DomainNameField.domain_name_validator)
        else:
            kwargs['validators'] = [DomainNameField.domain_name_validator]
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['max_length']
        if 'validators' in kwargs:
            if DomainNameField.domain_name_validator in kwargs['validators']:
                kwargs['validators'].remove(DomainNameField.domain_name_validator)
            if not kwargs['validators']:
                del kwargs['validators']
        return name, path, args, kwargs


class Zone(models.Model):
    name = DomainNameField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("zone")
        verbose_name_plural = _("zones")

class Record(PolymorphicModel):

    DNS_CLASSES = [
        (1, 'IN'),
        (2, 'CS'),
        (3, 'CH'),
        (4, 'HS')
    ]

    DNS_TYPES = [
        (  1, 'A'),
        (  2, 'NS'),
        (  5, 'CNAME'),
        (  6, 'SOA'),
        ( 12, 'PTR'),
        ( 15, 'MX'),
        ( 16, 'TXT'),
        ( 28, 'AAAA'),
        ( 33, 'SRV')
    ]

    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    name = RecordNameField()
    #type = models.PositiveIntegerField(choices=DNS_TYPES)
    clas = models.PositiveSmallIntegerField(choices=DNS_CLASSES, default=1, verbose_name="class")
    ttl = models.PositiveIntegerField(null=True)

    def save(self, *args, **kwargs):
        if not self.name.endswith('.' + self.zone.name) and self.name != self.zone.name:
            return
        super().save(*args, **kwargs)

    def clean(self):
        if not self.name.endswith('.' + self.zone.name) and self.name != self.zone.name:
            raise ValidationError(_("Record name must end with .{zone}.").format(zone=self.zone.name))

class A(Record):
    address = models.GenericIPAddressField(
        protocol='IPv4',
        verbose_name=_("address")
    )

    def __str__(self):
        return "A {address}".format(address=self.address)

    class Meta:
        verbose_name = _("A record")
        verbose_name_plural = _("A records")

class NS(Record):
    nsdname = DomainNameField(verbose_name=_("name server"))

    class Meta:
        verbose_name = _("NS record")
        verbose_name_plural = _("NS records")

class CNAME(Record):
    c_name = DomainNameField(verbose_name=_("canonical name"))

    def __str__(self):
        return "CNAME {c_name}".format(c_name=self.c_name)

    def save(self, *args, **kwargs):
        if Record.objects.filter(zone=self.zone, clas=self.clas, name=self.name):
            return
        super().save(*args, **kwargs)

    def clean(self):
        super().clean()
        if Record.objects.filter(zone=self.zone, clas=self.clas, name=self.name):
            raise ValidationError(_("A CNAME must be the only record for a name."))

    class Meta:
        verbose_name = _("CNAME record")
        verbose_name_plural = _("CNAME records")

class SOA(Record):
    mname = DomainNameField(verbose_name=_("main name server"))
    rname = models.EmailField(verbose_name=_("responsible email"))
    serial = models.BigIntegerField()
    refresh = models.BigIntegerField()
    retry = models.BigIntegerField()
    expire = models.BigIntegerField()
    minimum = models.BigIntegerField()

    def email_to_rname(self):
        rname = self.rname.split('@')
        return rname[0].replace('.', '\\.') + '.' + rname[1]

    def __str__(self):
        return "SOA {mname} {rname} {serial} {refresh} {retry} {expire} {minimum}".format(
            mname=self.mname,
            rname=self.email_to_rname(),
            serial=self.serial,
            refresh=self.refresh,
            retry=self.retry,
            expire=self.expire,
            minimum=self.minimum
        )

    class Meta:
        verbose_name = _("SOA record")
        verbose_name_plural = _("SOA records")

class PTR(Record):
    ptrdname = DomainNameField(verbose_name=_("pointer domain name"))

    def __str__(self):
        return "PTR {ptrdname}".format(ptrdname=self.ptrdname)

    class Meta:
        verbose_name = _("PTR record")
        verbose_name_plural = _("PTR records")

class MX(Record):
    preference = models.PositiveIntegerField()
    exchange = DomainNameField(verbose_name=_("exchange server"))

    def __str__(self):
        return "MX {preference} {exchange}".format(preference=self.preference, exchange=self.exchange)

    class Meta:
        verbose_name = _("MX record")
        verbose_name_plural = _("MX records")

class AAAA(Record):
    address = models.GenericIPAddressField(protocol='IPv6')

    def __str__(self):
        return "AAAA {address}".format(self.address)

    class Meta:
        verbose_name = _("AAAA record")
        verbose_name_plural = _("AAAA records")

class TXT(Record):
    data = models.TextField()

    def __str__(self):
        return "TXT {data!r}".format(data=self.data)

    class Meta:
        verbose_name = _("TXT record")
        verbose_name_plural = _("TXT records")

class SRV(Record):
    priority = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    port = models.PositiveIntegerField()
    target = DomainNameField()

    def __str__(self):
        return "SRV {priority} {weight} {port} {target}".format(
             priority=self.priority,
             weight=self.weight,
             port=self.port,
             target=self.target
        )

    class Meta:
        verbose_name = _("SRV record")
        verbose_name_plural = _("SRV records")

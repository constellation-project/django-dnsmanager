from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from polymorphic.models import PolymorphicModel

from .fields import RecordNameField, DomainNameField


class Zone(models.Model):
    name = DomainNameField(
        unique=True,
        verbose_name=_("name"),
    )

    def __str__(self):
        """
        String for autocompletion results and zone admin column
        """
        return self.name

    class Meta:
        verbose_name = _("zone")
        verbose_name_plural = _("zones")


class Record(PolymorphicModel):
    DNS_CLASSES = [
        ('IN', _("IN (Internet)")),
        ('CS', _("CS (CSNET, obsolete)")),
        ('CH', _("CH (CHAOS)")),
        ('HS', _("HS (Hesiod)")),
    ]

    zone = models.ForeignKey(
        Zone,
        on_delete=models.CASCADE,
        verbose_name=_("zone"),
        help_text=_("This record will be applied on that zone."),
    )
    name = RecordNameField(
        verbose_name=_("name"),
        blank=True,
    )
    dns_class = models.CharField(
        max_length=2,
        choices=DNS_CLASSES,
        default='IN',
        verbose_name=_("class"),
        help_text=_("You shouldn't need anything else than IN."),
    )
    ttl = models.PositiveIntegerField(
        null=True,
        default=3600,
        verbose_name=_("Time To Live"),
        help_text=_("Limits the lifetime of this record."),
    )

    class Meta:
        verbose_name = _("record")
        verbose_name_plural = _("records")


class A(Record):
    address = models.GenericIPAddressField(
        protocol='IPv4',
        verbose_name=_("IPv4 address")
    )

    def __str__(self):
        if self.name:
            return (f"{self.name}.{self.zone} {self.ttl} {self.dns_class} A "
                    f"{self.address}")
        else:
            return f"{self.zone} {self.ttl} {self.dns_class} A {self.address}"

    class Meta:
        verbose_name = _("A record")
        verbose_name_plural = _("A records")


class NS(Record):
    nsdname = DomainNameField(verbose_name=_("name server"))

    def __str__(self):
        return f"{self.zone} {self.ttl} {self.dns_class} NS {self.nsdname}"

    class Meta:
        verbose_name = _("NS record")
        verbose_name_plural = _("NS records")


class CNAME(Record):
    c_name = DomainNameField(
        verbose_name=_("canonical name"),
        help_text=_('This domain name will alias to this canonical name.'),
    )

    def __str__(self):
        return (f"{self.name}.{self.zone} {self.ttl} {self.dns_class} CNAME "
                f"{self.c_name}")

    def save(self, *args, **kwargs):
        cnames = Record.objects.filter(
            zone=self.zone, dns_class=self.dns_class, name=self.name)
        if cnames and any(cname.pk == self.pk for cname in cnames):
            return
        super().save(*args, **kwargs)

    def clean(self):
        super().clean()
        cnames = Record.objects.filter(
            zone=self.zone, dns_class=self.dns_class, name=self.name)
        if cnames and any(cname.pk == self.pk for cname in cnames):
            raise ValidationError(
                _("A CNAME must be the only record for a name."))

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
        """
        Convert email format to domain name format
        e.g. root@crans.org to root.crans.org
        """
        rname = self.rname.split('@')
        return rname[0].replace('.', '\\.') + '.' + rname[1]

    def __str__(self):
        rname = self.email_to_rname()
        return (f"{self.zone} {self.ttl} {self.dns_class} SOA {self.mname} "
                f"{rname} {self.serial} {self.refresh} {self.retry} "
                f"{self.expire} {self.minimum}")

    class Meta:
        verbose_name = _("SOA record")
        verbose_name_plural = _("SOA records")


class PTR(Record):
    ptrdname = DomainNameField(verbose_name=_("pointer domain name"))

    def __str__(self):
        return f"{self.ttl} {self.dns_class} PTR {self.ptrdname}"

    class Meta:
        verbose_name = _("PTR record")
        verbose_name_plural = _("PTR records")


class MX(Record):
    preference = models.PositiveIntegerField()
    exchange = DomainNameField(verbose_name=_("exchange server"))

    def __str__(self):
        return (f"{self.zone} {self.ttl} {self.dns_class} MX {self.preference}"
                f" {self.exchange}")

    class Meta:
        verbose_name = _("MX record")
        verbose_name_plural = _("MX records")


class AAAA(Record):
    address = models.GenericIPAddressField(
        protocol='IPv6',
        verbose_name=_("IPv6 address")
    )

    def __str__(self):
        if self.name:
            return (f"{self.name}.{self.zone} {self.ttl} {self.dns_class} AAAA"
                    f" {self.address}")
        else:
            return (f"{self.zone} {self.ttl} {self.dns_class} AAAA"
                    f" {self.address}")

    class Meta:
        verbose_name = _("AAAA record")
        verbose_name_plural = _("AAAA records")


class TXT(Record):
    data = models.TextField()

    def __str__(self):
        return f"{self.ttl} {self.dns_class} TXT {self.data!r}"

    class Meta:
        verbose_name = _("TXT record")
        verbose_name_plural = _("TXT records")


class SRV(Record):
    priority = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    port = models.PositiveIntegerField()
    target = DomainNameField()

    def __str__(self):
        return (f"{self.ttl} {self.dns_class} SRV {self.priority} "
                f"{self.weight} {self.port} {self.target}")

    class Meta:
        verbose_name = _("SRV record")
        verbose_name_plural = _("SRV records")

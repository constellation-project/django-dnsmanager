from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DnsManagerConfig(AppConfig):
    name = "dnsmanager"
    verbose_name = _("Domain Name System manager")

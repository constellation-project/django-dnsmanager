from django.contrib import admin
from django.urls import resolve
from polymorphic.admin import PolymorphicChildModelAdmin, \
    PolymorphicChildModelFilter, PolymorphicParentModelAdmin

from .models import A, AAAA, CAA, CNAME, DNAME, MX, NS, PTR, Record, \
    SOA, SRV, SSHFP, TXT, Zone


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    # For autocompletion
    search_fields = ('name', 'slug')

    # Autocomplete slug with name
    prepopulated_fields = {'slug': ('name', )}

    def get_model_perms(self, request):
        """
        Do not show zones admin in admin index as this isn't really useful
        Zone are created when creating the first record for this zone.
        """
        match = resolve(request.path)

        if match.app_name == 'admin' and match.url_name in ('index', 'app_list'):
            return {'add': False, 'change': False, 'delete': False}
        return super().get_model_perms(request)


@admin.register(Record)
class RecordAdmin(PolymorphicParentModelAdmin):
    base_model = Record
    child_models = (A, AAAA, CAA, CNAME, DNAME, MX, NS, PTR, SOA, SSHFP, SRV,
                    TXT)

    list_display = ('name', '__str__', 'zone')
    polymorphic_list = True
    list_filter = (PolymorphicChildModelFilter, 'dns_class', 'zone')
    search_fields = ('name', 'zone__name')


@admin.register(A)
class AAdmin(PolymorphicChildModelAdmin):
    base_model = A
    autocomplete_fields = ('zone',)


@admin.register(AAAA)
class AAAAAdmin(PolymorphicChildModelAdmin):
    base_model = AAAA
    autocomplete_fields = ('zone',)


@admin.register(CAA)
class CAAAdmin(PolymorphicChildModelAdmin):
    base_model = CAA
    autocomplete_fields = ('zone',)


@admin.register(CNAME)
class CNAMEAdmin(PolymorphicChildModelAdmin):
    base_model = CNAME
    autocomplete_fields = ('zone',)


@admin.register(DNAME)
class DNAMEAdmin(PolymorphicChildModelAdmin):
    base_model = DNAME
    autocomplete_fields = ('zone',)


@admin.register(MX)
class MXAdmin(PolymorphicChildModelAdmin):
    base_model = MX
    autocomplete_fields = ('zone',)


@admin.register(NS)
class NSAdmin(PolymorphicChildModelAdmin):
    base_model = NS
    autocomplete_fields = ('zone',)


@admin.register(PTR)
class PTRAdmin(PolymorphicChildModelAdmin):
    base_model = PTR
    autocomplete_fields = ('zone',)


@admin.register(SOA)
class SOAAdmin(PolymorphicChildModelAdmin):
    base_model = SOA
    autocomplete_fields = ('zone',)


@admin.register(SSHFP)
class SSHFPAdmin(PolymorphicChildModelAdmin):
    base_model = SSHFP
    autocomplete_fields = ('zone',)


@admin.register(SRV)
class SRVAdmin(PolymorphicChildModelAdmin):
    base_model = SRV
    autocomplete_fields = ('zone',)


@admin.register(TXT)
class TXTAdmin(PolymorphicChildModelAdmin):
    base_model = TXT
    autocomplete_fields = ('zone',)


class AInline(admin.TabularInline):
    extra = 0
    model = A


class AAAAInline(admin.TabularInline):
    extra = 0
    model = AAAA


class CNAMEInline(admin.TabularInline):
    extra = 0
    model = CNAME


class PTRInline(admin.TabularInline):
    extra = 0
    model = PTR

from django.contrib import admin
from polymorphic.admin import PolymorphicChildModelAdmin, \
    PolymorphicChildModelFilter, PolymorphicParentModelAdmin

from .models import Zone, Record, \
    A, NS, CNAME, SOA, PTR, MX, AAAA, TXT, SRV

@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    pass

@admin.register(Record)
class RecordAdmin(PolymorphicParentModelAdmin):
    base_model = Record
    child_models = (A, NS, CNAME, SOA, PTR, MX, AAAA, TXT, SRV)

    list_display = ('name', 'clas', '__str__', 'zone')
    polymorphic_list = True

@admin.register(A)
class AAdmin(PolymorphicChildModelAdmin):
    base_model = A

@admin.register(NS)
class NSAdmin(PolymorphicChildModelAdmin):
    base_model = NS

@admin.register(CNAME)
class CNAMEAdmin(PolymorphicChildModelAdmin):
    base_model = CNAME

@admin.register(SOA)
class SOAAdmin(PolymorphicChildModelAdmin):
    base_model = SOA

@admin.register(PTR)
class PTRAdmin(PolymorphicChildModelAdmin):
    base_model = PTR

@admin.register(MX)
class MXAdmin(PolymorphicChildModelAdmin):
    base_model = MX

@admin.register(AAAA)
class AAAAAdmin(PolymorphicChildModelAdmin):
    base_model = AAAA

@admin.register(TXT)
class TXTAdmin(PolymorphicChildModelAdmin):
    base_model = TXT

@admin.register(SRV)
class SRVAdmin(PolymorphicChildModelAdmin):
    base_model = SRV


class AInline(admin.TabularInline):
    extra = 0
    model = A

class CNAMEInline(admin.TabularInline):
    extra = 0
    model = CNAME

class PTRInline(admin.TabularInline):
    extra = 0
    model = PTR

class AAAAInline(admin.TabularInline):
    extra = 0
    model = AAAA

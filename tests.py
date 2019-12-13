from django.test import TestCase

from .models import A, AAAA, CNAME, NS, MX, SOA, Zone

"""
Test DNS app against some records from Cr@ns.
"""


class DnsTestCase(TestCase):
    def setUp(self):
        self.zone = Zone.objects.create(name="crans.org.")
        A.objects.create(
            zone=self.zone,
            address="185.230.79.194",
            ttl=3600,
        )
        AAAA.objects.create(
            zone=self.zone,
            address="2a0c:700:0:24:ba:ccff:feda:aa00",
            ttl=3600,
        )
        CNAME.objects.create(
            zone=self.zone,
            name="demo",
            c_name="demo.adh.crans.org.",
            ttl=3600,
        )
        NS.objects.create(
            zone=self.zone,
            nsdname="silice.crans.org.",
            ttl=3599,
        )
        MX.objects.create(
            zone=self.zone,
            preference=10,
            exchange="redisdead.crans.org.",
            ttl=3600,
        )
        SOA.objects.create(
            zone=self.zone,
            mname="silice.crans.org.",
            rname="root@crans.org.",
            serial=3654784651,
            refresh=76400,
            retry=5000,
            expire=3500000,
            minimum=3600,
            ttl=3600,
        )

    def test_a(self):
        """Verify A"""
        a = A.objects.get(address="185.230.79.194", zone=self.zone)
        self.assertEqual(
            str(a),
            "crans.org. 3600 IN A 185.230.79.194"
        )

    def test_aaaa(self):
        """Verify AAAA"""
        aaaa = AAAA.objects.get(
            address="2a0c:700:0:24:ba:ccff:feda:aa00", zone=self.zone)
        self.assertEqual(
            str(aaaa),
            "crans.org. 3600 IN AAAA 2a0c:700:0:24:ba:ccff:feda:aa00"
        )

    def test_cname(self):
        """Verify CNAME"""
        cname = CNAME.objects.get(name="demo", zone=self.zone)
        self.assertEqual(
            str(cname),
            "demo.crans.org. 3600 IN CNAME demo.adh.crans.org."
        )

    def test_ns(self):
        """Verify NS"""
        ns = NS.objects.get(nsdname="silice.crans.org.", zone=self.zone)
        self.assertEqual(
            str(ns),
            "crans.org. 3599 IN NS silice.crans.org."
        )

    def test_mx(self):
        """Verify MX"""
        mx = MX.objects.get(exchange="redisdead.crans.org.", zone=self.zone)
        self.assertEqual(
            str(mx),
            "crans.org. 3600 IN MX 10 redisdead.crans.org."
        )

    def test_soa(self):
        """Verify SOA"""
        soa = SOA.objects.get(mname="silice.crans.org.", zone=self.zone)
        self.assertEqual(
            str(soa),
            "crans.org. 3600 IN SOA silice.crans.org. root.crans.org. 3654784651 76400 5000 3500000 3600"
        )

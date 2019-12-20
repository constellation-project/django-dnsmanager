from django.contrib.auth.models import User
from django.test import TestCase

from ..models import A, AAAA, CNAME, MX, NS, SOA, Zone

"""
Test that views work
"""


class ViewsTestCase(TestCase):
    def setUp(self):
        self.zone = Zone.objects.create(
            name="crans.org",
            slug="cransorg",
        )
        A.objects.create(
            zone=self.zone,
            name="@",
            address="185.230.79.194",
            ttl=3600,
        )
        AAAA.objects.create(
            zone=self.zone,
            name="@",
            address="2a0c:700:0:24:ba:ccff:feda:aa00",
            ttl=3600,
        )
        CNAME.objects.create(
            zone=self.zone,
            name="demo",
            c_name="demo.adh.crans.org.",
            ttl=3600,
        )
        MX.objects.create(
            zone=self.zone,
            name="@",
            preference=10,
            exchange="redisdead.crans.org.",
            ttl=3600,
        )
        NS.objects.create(
            zone=self.zone,
            name="@",
            nsdname="silice.crans.org.",
            ttl=3599,
        )
        SOA.objects.create(
            zone=self.zone,
            name="@",
            mname="silice.crans.org.",
            rname="root@crans.org",
            serial=3654784651,
            refresh=76400,
            retry=5000,
            expire=3500000,
            minimum=3600,
            ttl=3600,
        )

        # Login as admin
        self.user = User.objects.create_superuser(
            username="admin",
            password="adminadmin",
            email="admin@example.com",
        )
        self.client.force_login(self.user)

    def test_zone_view(self):
        """
        Check that zone view work
        """
        response = self.client.get('/cransorg/')
        self.assertEqual(response.status_code, 200)

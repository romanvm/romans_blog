from django.test import TestCase
from .models import SiteConfiguration


class MaintenanceModeTestCase(TestCase):
    def test_maintenance_mode(self):
        site_config = SiteConfiguration(maintenance_mode=True)
        site_config.save()
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 503)

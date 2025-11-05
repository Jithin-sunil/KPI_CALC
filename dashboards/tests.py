from django.test import TestCase
from django.urls import reverse

class DashboardViewsTest(TestCase):
    def test_dashboard_view(self):
        response = self.client.get(reverse('kpi_dashboard', args=['emp1']))
        self.assertEqual(response.status_code, 200)
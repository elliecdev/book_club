from rest_framework.test import APITestCase
from django.urls import reverse


class HealthCheckTest(APITestCase):
    def test_health_endpoint(self):
        url = reverse("health")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["status"], "ok")
        self.assertEqual(response.data["database"], "ok")

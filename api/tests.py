from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class AccountTests(APITestCase):
    def test_create_user(self):
        url = reverse('user-list')
        data = {'telephone': '1929839', 'password': 'DabApps', }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

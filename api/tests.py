from rest_framework import status
from rest_framework.test import APITestCase

from api.models import User


class UserTests(APITestCase):
    def setUp(self):
        User.objects.create(telephone="lion", password="roar", is_admin=True)
        User.objects.create(telephone="cat", password="meow", is_admin=True)

    def test_create_user(self):
        url = "/api/users/"
        data = {'telephone': '1929839', 'password': 'DabApps', 'is_admin': True}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 3)
        self.assertEqual(User.objects.get(telephone='1929839').password, data['password'])

    def test_update_user(self):
        user = User.objects.get(telephone="lion")
        self.client.login(telephone="110", password="wasai123")
        url = "/api/users/" + str(user.id) + "/"
        data = {'is_admin': False}
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(user.is_admin, data['is_admin'])

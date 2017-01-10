from rest_framework import status
from rest_framework.test import APITestCase


class UserTests(APITestCase):
    def test_create_user(self):
        self.assertEqual(201, status.HTTP_201_CREATED)

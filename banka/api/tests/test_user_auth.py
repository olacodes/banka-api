from django.urls import reverse

from rest_framework import status 
from rest_framework.test import APITestCase

from .mock_data.user_data import UserData


class TestUserAuth(APITestCase):
    def test_user_signup(self):
        url = reverse('signup')
        print(url)
        response = self.client.post(url, UserData.user_signup_data())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['data']['lastname'], 'testing')


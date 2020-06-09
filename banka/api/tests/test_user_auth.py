from django.urls import reverse

from rest_framework import status 
from rest_framework.test import APITestCase

from .mock_data.user_data import UserData


class TestUserAuth(APITestCase):
    def test_user_signup(self):
        url = reverse('signup')
        response = self.client.post(url, UserData.user_signup_data())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['data']['lastname'], 'testing')

    def test_user_sign_in(self):
        self.test_user_signup()
        url = reverse('signin')
        response = self.client.post(url, UserData.user_signup_data())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['firstname'], 'test')
        self.assertEqual(response.data['data']['lastname'], 'testing')




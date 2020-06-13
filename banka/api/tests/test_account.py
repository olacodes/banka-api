from django.urls import reverse

from rest_framework import status 
from rest_framework.test import APITestCase

from .mock_data.mock_data import create_account, sign_up_data
from ..models.user import User


class TestAccount(APITestCase):
    def test_create_account(self):
        user = User.objects.create(**sign_up_data())
        url = reverse('accounts')
        response = self.client.post(url, create_account(user.id))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


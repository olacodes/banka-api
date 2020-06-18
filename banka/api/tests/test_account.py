from django.urls import reverse

from rest_framework import status 
from rest_framework.test import APITestCase

from .mock_data.mock_data import create_account, sign_up_data, update_account
from ..models.user import User
from ..models.account import Account

class TestAccount(APITestCase):
    def test_create_account(self):
        user = User.objects.create(**sign_up_data())
        url = reverse('accounts')
        response = self.client.post(url, create_account(user.id))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return response.data

    def test_update_account(self):
        get_acc = self.test_create_account()
        acc_num = get_acc['data']['account_number']
        url = f'/api/v1/accounts/{acc_num}/'
        response = self.client.put(url, update_account(), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


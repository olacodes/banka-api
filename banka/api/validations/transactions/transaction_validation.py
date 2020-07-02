from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError

from ...models.user import User
from ...models.account import Account
from ...models.transaction import Transaction
from ...utils.api_response import APIResponse
from .transaction_field import TransactionFieldValidation


def validate_transaction(data, account_number):
    api_response = APIResponse()

    # account_number
    if TransactionFieldValidation.validate_account_number_exist(account_number, Account) == False:
        APIResponse.set_error(
            api_response, 400, 'Account number does not exist', 'Invalid account number')
        return APIResponse.send(api_response)

    # validate cashier
    if TransactionFieldValidation.validate_cashier(data, User) == False:
        APIResponse.set_error(
            api_response, 400, 'Only staff can perform this operation', 'Only staff is allowed to perform this operation'
        )
        return APIResponse.send(api_response)

    # validate transaction type
    if TransactionFieldValidation.validate_transaction_type(data) == False:
        APIResponse.set_error(api_response, 400, 'Transaction can only be credit or debit', 'Invalid transaction type')
        return APIResponse.send(api_response)

    # validate amount
    if TransactionFieldValidation.validate_amount(data) == False:
        APIResponse.set_error(
            api_response, 400, 'Please provide a valid amount', 'Invalid amount')
        return APIResponse.send(api_response)

    print('All fields are satisfied')


    return True

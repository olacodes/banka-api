import uuid
from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ...utils.api_response import APIResponse
from ...models.account import Account
from ...models.user import User
from ...serializers.account_serializer import AccountSerializer
from ...serializers.transaction_serializer import TransactionSerializer
from ...validations.transactions.transaction_validation import validate_transaction


class DebitTransaction(APIView):
    '''
    POST /transactions/<account_number>/debit
    '''
    api_response = APIResponse()
    # Take out the person account

    def post(self, request, account_number, format=None):
        data = request.data
        data = data.copy()
        data['transaction_type'] = 'debit'

        # validate input data
        valid_transaction = validate_transaction(data, account_number)
        if valid_transaction != True:
            return valid_transaction

        account = get_object_or_404(Account, account_number=account_number)

        # validate amount
        old_balance = account.balance
        debit_amount = data['amount']

        if debit_amount > old_balance:
            APIResponse.set_error(self.api_response, 400,
                                  'Insufficient balance', 'Insufficient balance')
            return APIResponse.send(self.api_response)

        new_balance = old_balance - debit_amount
        account_balance = {'balance': new_balance}

        acc_serializer = AccountSerializer(
            account, data=account_balance, partial=True)

        if not acc_serializer.is_valid():
            return Response(acc_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        acc_serializer.save()

        data['old_balance'] = old_balance
        data['new_balance'] = new_balance
        data['account_number'] = account_number
        data['cashier'] = data['cashier']

        transaction_serializer = TransactionSerializer(data=data)
        if transaction_serializer.is_valid():
            transaction_serializer.save()
            res_data = transaction_serializer.data
            print(res_data)
            return Response({
                'status': 200,
                'message': 'Account successfully debited',
                'data': {
                    'transaction_id': res_data['id'],
                    'account_number': res_data['account_number'],
                    'amount': res_data['amount'],
                    'balance': res_data['new_balance'],
                    'cashier': res_data['cashier'],
                    'transaction_type': res_data['transaction_type']
                }
            })
        return Response(transaction_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreditTransaction(APIView):
    '''
    POST /transactions/<account_number>/credit
    '''
    api_response = APIResponse

    def post(self, request, account_number, format=None):
        data = request.data
        data = data.copy()
        data['transaction_type'] = 'credit'

        # validate input data
        valid_transaction = validate_transaction(data, account_number)
        if valid_transaction != True:
            return valid_transaction

        account = get_object_or_404(Account, account_number=account_number)

        # validate amount
        old_balance = account.balance
        credit_amount = data['amount']

        new_balance = old_balance + credit_amount
        account_balance = {'balance': new_balance}

        acc_serializer = AccountSerializer(
            account, data=account_balance, partial=True)

        if not acc_serializer.is_valid():
            return Response(acc_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        acc_serializer.save()

        data['old_balance'] = old_balance
        data['new_balance'] = new_balance
        data['account_number'] = account_number
        data['cashier'] = data['cashier']

        transaction_serializer = TransactionSerializer(data=data)
        if transaction_serializer.is_valid():
            transaction_serializer.save()
            res_data = transaction_serializer.data
            return Response({
                'status': 200,
                'message': 'Account successfully credited',
                'data': {
                    'transaction_id': res_data['id'],
                    'account_number': res_data['account_number'],
                    'amount': res_data['amount'],
                    'balance': res_data['new_balance'],
                    'cashier': res_data['cashier'],
                    'transaction_type': res_data['transaction_type']
                }
            })
        return Response(transaction_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ...models.user import User
from ...models.account import Account
from ...validations.accounts.account_validation import validate_account
from ...utils.helper import Helper


class AccountView(APIView):
    def post(self, request):
        # Create Account
        data = request.data

        # Generate Account number
        account_number = Helper.create_account_num(Account)
        # Add account number to the data object
        data['account_number'] = account_number

        # Validate all account fields
        valid_account = validate_account(data)
        if valid_account != True:
            return valid_account

        # get owner id
        owner = User.objects.get(id=data['user_id'])

        # Generate account id
        id = uuid.uuid4()

        # create Account object
        account = Account.objects.create(
            id=id,
            account_number=account_number,
            owner=owner,
            account_type=data['account_type'],
            account_status=data['account_status'],
            balance=data['balance']
        )

        # save account in db
        account.save()

        # select the newly created account from DB
        new_account = Account.objects.filter(id=id)[0]

        # create return object
        return Response({
            'status': 201,
            'data': {
                'account_number': new_account.account_number,
                'firstname': owner.firstname,
                'lastname': owner.lastname,
                'email': owner.email,
                'account_type': new_account.account_type,
                'opening_balance': new_account.balance
            }
        }, status=status.HTTP_201_CREATED)

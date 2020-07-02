from django.shortcuts import get_object_or_404
from ...models.user import User

from ...utils.helper import Helper


class TransactionFieldValidation:
    @staticmethod
    def validate_account_number_exist(account_num, model):
        account_exist = Helper.get_account_number(model, int(account_num))
        return account_exist

    @staticmethod
    def validate_cashier(data, model):
        cashier_id = Helper.get_field(data, 'cashier')
        try:
            cashier_exist = get_object_or_404(
                model, user_type='staff', pk=cashier_id)
            return cashier_exist
        except:
            return False

    @staticmethod
    def validate_amount(data):
        amount = Helper.get_field(data, 'amount')
        return True if Helper.is_decimal(amount) else False

    @staticmethod
    def transaction_type(value):
        try:
            transaction = value.lower()
            if transaction == "credit" or transaction == "debit":
                return True
            return False
        except:
            return False

    @classmethod
    def validate_transaction_type(cls, data):
        transaction_type = Helper.get_field(data, 'transaction_type')
        trans_type = cls.transaction_type(transaction_type)
        return trans_type

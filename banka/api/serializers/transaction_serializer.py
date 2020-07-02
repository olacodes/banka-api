from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from ..models.transaction import Transaction


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('id', 'created_on', 'transaction_type', 'account_number',
                  'cashier', 'amount', 'old_balance', 'new_balance')
                  
    def validate_transaction_type(self, value):
        value = (value.lower()).strip()
        if not (value == 'debit' or value == 'credit'):
            serializers.ValidationError({
                'Invalid transaction type': _('Transaction type can only be debit or credit')
            })
        return value

import uuid
from django.db import models
from .user import User


class Transaction(models.Model):
    """
    This model create a transaction database table with the following fields and 
    has a oneOnOne-relationship with the User(staff(cashier)) that consummated the transaction
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_on = models.DateTimeField(auto_now=True)
    transaction_type = models.CharField(max_length=40, null=False) # credit or debit
    account_number = models.BigIntegerField(null=False)
    cashier = models.ForeignKey(User, on_delete=models.CASCADE, null=False) # cashier who consummated the transaction
    amount = models.DecimalField(max_digits=250, decimal_places=2, null=False)
    old_balance = models.DecimalField(max_digits=250, decimal_places=2, null=False)
    new_balance = models.DecimalField(max_digits=250, decimal_places=2, null=False)

    
    def __str__(self):
        return self.id

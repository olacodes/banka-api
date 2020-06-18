import uuid
from django.db import models

from .user import User
from ..validations.accounts.account_validation import validate_account_status, validate_account_type


class Account(models.Model):
    """
    This model creates account table in the database with the following fields and
    has oneToMany-relationship with User(client) owner of the account
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account_number = models.BigIntegerField(null=False)
    created_on = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    account_type = models.CharField(
        validators=[validate_account_type], max_length=20)  # savings or current
    account_status = models.CharField(validators=[validate_account_status],
                                      max_length=20, null=False)  # draft, active, dormant
    balance = models.DecimalField(
        max_digits=250, decimal_places=2, default=0.00)

    def __str__(self):
        return self.account_number

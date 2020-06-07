from django.db import models
from .user import User


class Account(models.Model):
    """
    This model creates account table in the database with the following fields and
    has oneToMany-relationship with User(client) owner of the account
    """
    account_number = models.IntegerField(max_length=20, null=False)
    created_on = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    account_type = models.CharField(max_length=20, null=False) # savings or current
    status = models.CharField(max_length=20, null=False) # draft, active, dormant
    balance = models.DecimalField(max_digits=250, decimal_places=2, default=0.00)

    def __str__(self):
        return self.account_number


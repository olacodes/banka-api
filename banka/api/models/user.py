import uuid
from django.db import models


class User(models.Model):
    """
    This model creates User table in the database with the following fields 
    and makes email unique
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(null=False, unique=True)
    firstname = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=250, null=False)
    user_type = models.CharField(default='client', max_length=10, null=False) # client or staff
    is_admin = models.BooleanField(default=False) # Must be a staff user account
    created_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.firstname

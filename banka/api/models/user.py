from django.db import models


class User(models.Model):
    """
    This model creates User table in the database with the following fields 
    and makes email unique
    """
    email = models.EmailField(null=False, unique=True)
    firstname = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=250, null=False)
    user_type = models.CharField(max_length=10, null=False) # client or staff
    isAdmin = models.BooleanField(default=False) # Must be a staff user account
    
    def __str__(self):
        return self.firstname

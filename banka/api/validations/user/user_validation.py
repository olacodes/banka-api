from .user_field_validation import UserFieldValidation
from rest_framework.response import Response
from rest_framework import status

def validate_user(data):

    if UserFieldValidation.validate_firstname(data) == False:
        return Response({
            'status': 400, 
            'message': 'username must not be less than 2 characters',
            'error': "Invalid Username"
        },status=status.HTTP_400_BAD_REQUEST)

    if UserFieldValidation.validate_lastname(data) == False:
        return Response({
        'status': 400,
        'message': 'lastname must not be less than 2 characters', 
        'error': "Invalid lastname"
    },status=status.HTTP_400_BAD_REQUEST)

    if UserFieldValidation.validate_email(data) == False:
        return Response({
            'status': 400,
            'message': 'please provide a valid email', 
            'error': "Invalid Email"
        },status=status.HTTP_400_BAD_REQUEST)

    if UserFieldValidation.validate_password(data) == False:
        return Response({
        'status': 400,
        'message': 'password must not be less than 5 characters', 
        'error': "Invalid password"
    },status=status.HTTP_400_BAD_REQUEST)
    
    if UserFieldValidation.validate_user_type(data) == False:
        return Response({
        'status': 400,
        'message': 'user_type can only be staff or client', 
        'error': "Invalid user_type"
    },status=status.HTTP_400_BAD_REQUEST)
    
    if UserFieldValidation.validate_is_admin(data) == False:
        return Response({
        'status': 400,
        'message': 'is_admin can only be true or false', 
        'error': "Invalid is_admin"
    },status=status.HTTP_400_BAD_REQUEST)

    return True;

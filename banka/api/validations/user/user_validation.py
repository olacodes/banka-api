from rest_framework.response import Response
from rest_framework import status

from .user_field_validation import UserFieldValidation
from ...utils.api_response import APIResponse


def validate_user(data):
    api_response = APIResponse()

    if UserFieldValidation.validate_firstname(data) == False:
        APIResponse.set_error(
            api_response, 400, 'firstname must not be less than 2 characters or empty', "Invalid firstname")
        return APIResponse.send(api_response)

    if UserFieldValidation.validate_lastname(data) == False:
        APIResponse.set_error(
            api_response, 400, 'lastname must not be less than 2 characters or empty', "Invalid lastname")
        return APIResponse.send(api_response)

    if UserFieldValidation.validate_email(data) == False:
        APIResponse.set_error(
            api_response, 400, 'please provide a valid email',  "Invalid email")
        return APIResponse.send(api_response)

    if UserFieldValidation.validate_password(data) == False:
        APIResponse.set_error(
            api_response, 400, 'password must not be less than 5 characters or empty',  "Invalid password")
        return APIResponse.send(api_response)

    if UserFieldValidation.validate_user_type(data) == False:
        APIResponse.set_error(
            api_response, 400,  'user_type can only be staff or client',  "Invalid user_type")
        return APIResponse.send(api_response)

    if UserFieldValidation.validate_is_admin(data) == False:
        APIResponse.set_error(
            api_response, 400,  'is_admin can only be true or false',  "Invalid is_admin")
        return APIResponse.send(api_response)

    return True

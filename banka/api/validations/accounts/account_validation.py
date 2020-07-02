from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .account_field_validation import AccountFieldValidation
from ...models.user import User
from ...utils.api_response import APIResponse


def validate_account(data):
    api_response = APIResponse()
    # account_number
    if AccountFieldValidation.validate_account_number(data) == False:
        APIResponse.set_error(
            api_response, 400, 'Account number must be of 10 digits', 'Invalid account number')
        APIResponse.send(api_response)

    # owner
    if AccountFieldValidation.validate_owner(User, data) == False:
        APIResponse.set_error(
            api_response, 400, 'Invalid account owner', 'Invalid account owner')
        return APIResponse.send(api_response)

    # account_type
    if AccountFieldValidation.validate_account_type(data) == False:
        APIResponse.set_error(
            api_response, 400, 'Account type must either be savings or current', 'Invalid account type')
        return APIResponse.send(api_response)

    # status
    if AccountFieldValidation.validate_account_status(data) == False:
        APIResponse.set_error(
            api_response, 400, 'Account status must either be draft, active or dormant', 'Invalid account status')
        return APIResponse.send(api_response)

    # balance
    if AccountFieldValidation.validate_account_balance(data) == False:
        APIResponse.set_error(
            api_response, 400, 'Account balance be a decimal number', 'Invalid account balance')
        return APIResponse.send(api_response)

    return True


def validate_account_type(value):
    value = value.lower().strip()
    if not (value == 'savings' or value == 'current'):
        raise ValidationError(
            _('account type can only be savings or current'),
            params={'value': value},
        )


def validate_account_status(value):
    value = value.lower().strip()
    if not (value == 'draft' or value == 'active' or value == 'dormant'):
        raise ValidationError(
            _('account status can only be active or dormant or draft'),
            params={'value': value}
        )

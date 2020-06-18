from ...utils.helper import Helper


class AccountFieldValidation:
    @staticmethod
    def account_type_value(value):
        try:
            value_to_lower = value.lower()
            if value_to_lower == "current" or value_to_lower == "savings":
                return value_to_lower
            return False
        except:
            return False

    @classmethod
    def validate_account_type(cls, data):
        # Must either be current or savings and not empty
        account_type = Helper.get_field(data, 'account_type')
        is_valid_account_type = cls.account_type_value(account_type)
        return is_valid_account_type

    @staticmethod
    def account_status_value(value):
        try:
            status_value = value.lower()
            if status_value == "draft" or status_value == "active" or status_value == "dormant":
                return status_value
            return False
        except:
            return False

    @classmethod
    def validate_account_status(cls, data):
        # must either be draft, active or dormant and not empty
        account_status = Helper.get_field(data, 'account_status')
        validate_status = cls.account_status_value(account_status)
        return validate_status

    @staticmethod
    def validate_account_number(data):
        # must be ten digit long and not empty
        account_number = Helper.get_field(data, 'account_number')
        return account_number if Helper.absolute_length(account_number, 10) else False

    @staticmethod
    def validate_account_balance(data):
        # must not be empty and Must be a decimal number
        account_balance = Helper.get_field(data, 'balance')
        return True if Helper.is_decimal(account_balance) else False

    @staticmethod
    def validate_owner(model, data):
        # should not be empty and must be a valid user_id
        owner_id = Helper.get_field(data, 'user_id')
        try:
            id = model.objects.get(id=owner_id)
            return id
        except:
            return False

    @classmethod
    def validate_account_number_exist(cls, data, model):
        account_number = cls.validate_account_number(data)
        # check if account number exist in db
        if not account_number:
            return False
        return Helper.get_from_DB(model, 'account_number', int(account_number))
